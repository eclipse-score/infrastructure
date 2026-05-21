(function () {
    function normalizeText(value) {
        return (value || "")
            .replace(/\u00a0/g, " ")
            .replace(/\s+/g, " ")
            .trim();
    }

    function canonicalText(value) {
        return normalizeText(value)
            .toLowerCase()
            .replace(/<br\s*\/?>/gi, " ")
            .replace(/&amp;/gi, " and ")
            .replace(/[^0-9a-z]+/g, "");
    }

    function hasNodeShape(group) {
        return Boolean(group.querySelector("rect, circle, ellipse, polygon, path"));
    }

    function candidateGroups(svg, wantedText) {
        const wanted = canonicalText(wantedText);
        if (!wanted) {
            return [];
        }

        const matches = new Set();
        for (const element of svg.querySelectorAll("*")) {
            if (canonicalText(element.textContent) !== wanted) {
                continue;
            }

            let current = element;
            while (current && current !== svg) {
                if (current.tagName && current.tagName.toLowerCase() === "g" && hasNodeShape(current)) {
                    matches.add(current);
                    break;
                }
                current = current.parentElement;
            }
        }

        return Array.from(matches).sort(
            (left, right) => left.querySelectorAll("*").length - right.querySelectorAll("*").length
        );
    }

    function bindLink(group, link) {
        if (group.dataset.chapterMapHref === link.href) {
            return;
        }

        group.dataset.chapterMapHref = link.href;
        group.dataset.chapterMapKind = link.kind || "section";
        group.classList.add("chapter-map-node-link", `chapter-map-node-${group.dataset.chapterMapKind}`);
        group.setAttribute("role", "link");
        group.setAttribute("tabindex", "0");

        const open = function () {
            window.location.assign(link.href);
        };

        group.addEventListener("click", function (event) {
            event.preventDefault();
            open();
        });

        group.addEventListener("keydown", function (event) {
            if (event.key !== "Enter" && event.key !== " ") {
                return;
            }
            event.preventDefault();
            open();
        });
    }

    function enhanceDiagram(diagram, links) {
        const svg = diagram.querySelector("svg");
        if (!svg) {
            return false;
        }

        let boundCount = 0;
        for (const link of links) {
            const texts = Array.isArray(link.match_texts) ? link.match_texts : [link.title];
            let target = null;

            for (const text of texts) {
                const candidates = candidateGroups(svg, text);
                if (candidates.length > 0) {
                    target = candidates[0];
                    break;
                }
            }

            if (!target) {
                continue;
            }

            bindLink(target, link);
            boundCount += 1;
        }

        diagram.classList.toggle("chapter-map-enhanced", boundCount > 0);
        return boundCount > 0;
    }

    function diagramForScript(script) {
        let current = script.previousElementSibling;
        while (current) {
            if (current.classList && current.classList.contains("mermaid")) {
                return current;
            }
            current = current.previousElementSibling;
        }
        return null;
    }

    function waitForSvg(diagram, callback) {
        const existing = diagram.querySelector("svg");
        if (existing) {
            callback();
            return;
        }

        const observer = new MutationObserver(function () {
            if (!diagram.querySelector("svg")) {
                return;
            }
            observer.disconnect();
            callback();
        });

        observer.observe(diagram, { childList: true, subtree: true });
    }

    function scheduleRetry() {
        window.setTimeout(initializeMindmaps, 250);
        window.setTimeout(initializeMindmaps, 1000);
    }

    function initializeMindmaps() {
        for (const script of document.querySelectorAll(".chapter-map-links-data")) {
            if (script.dataset.chapterMapInitialized === "true") {
                continue;
            }

            const diagram = diagramForScript(script);
            if (!diagram) {
                continue;
            }

            let links;
            try {
                links = JSON.parse(script.textContent || "[]");
            } catch (_error) {
                continue;
            }

            if (diagram.querySelector("svg")) {
                if (enhanceDiagram(diagram, links)) {
                    script.dataset.chapterMapInitialized = "true";
                } else {
                    scheduleRetry();
                }
                continue;
            }

            if (script.dataset.chapterMapWaiting === "true") {
                continue;
            }

            script.dataset.chapterMapWaiting = "true";
            waitForSvg(diagram, function () {
                script.dataset.chapterMapWaiting = "false";
                if (enhanceDiagram(diagram, links)) {
                    script.dataset.chapterMapInitialized = "true";
                } else {
                    scheduleRetry();
                }
            });
        }
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initializeMindmaps);
    } else {
        initializeMindmaps();
    }

    window.addEventListener("load", initializeMindmaps);
    window.setTimeout(initializeMindmaps, 250);
    window.setTimeout(initializeMindmaps, 1000);
})();
