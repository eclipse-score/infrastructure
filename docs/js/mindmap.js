(function () {
    "use strict";

    const DEFAULT_SCALE = 1.2;
    const MIN_SCALE = 0.6;
    const MAX_SCALE = 3;
    const SCALE_STEP = 0.2;

    function clamp(value, minimum, maximum) {
        return Math.min(Math.max(value, minimum), maximum);
    }

    function escapeSelector(value) {
        if (window.CSS && typeof window.CSS.escape === "function") {
            return window.CSS.escape(value);
        }
        return value.replace(/[^a-zA-Z0-9_-]/g, "\\$&");
    }

    function normalizeLabel(value) {
        return value.replace(/\s+/g, " ").trim();
    }

    function openHref(href) {
        window.location.href = href;
    }

    function makeNodeInteractive(element, href, label) {
        if (!element || element.dataset.mindmapHref === href) {
            return;
        }

        element.dataset.mindmapHref = href;
        element.classList.add("mindmap-clickable");
        element.setAttribute("tabindex", "0");
        element.setAttribute("role", "link");
        if (label) {
            element.setAttribute("aria-label", `Open ${label}`);
        }

        element.addEventListener("click", function () {
            openHref(href);
        });
        element.addEventListener("keydown", function (event) {
            if (event.key !== "Enter" && event.key !== " ") {
                return;
            }
            event.preventDefault();
            openHref(href);
        });
    }

    function findNodeElement(svg, nodeId, label) {
        const byId = svg.querySelector(`#${escapeSelector(nodeId)}`);
        if (byId) {
            return byId;
        }

        const labelNodes = svg.querySelectorAll("text, tspan, span, foreignObject");
        for (const labelNode of labelNodes) {
            if (normalizeLabel(labelNode.textContent || "") !== label) {
                continue;
            }
            const group = labelNode.closest("g[id]") || labelNode.closest("g");
            if (group) {
                return group;
            }
        }

        return null;
    }

    function updateScaleLabel(toolbar, scale) {
        if (!toolbar) {
            return;
        }
        const scaleLabel = toolbar.querySelector(".mindmap-scale");
        if (scaleLabel) {
            scaleLabel.textContent = `${Math.round(scale * 100)}%`;
        }
    }

    function fitScale(shell, state) {
        if (!state.baseWidth) {
            return state.scale;
        }
        const availableWidth = Math.max(shell.clientWidth - 24, 240);
        return clamp(availableWidth / state.baseWidth, MIN_SCALE, MAX_SCALE);
    }

    function applyScale(shell, toolbar, state) {
        if (!state.svg || !state.baseWidth || !state.baseHeight) {
            return;
        }

        state.scale = clamp(state.scale, MIN_SCALE, MAX_SCALE);
        state.svg.style.width = `${Math.round(state.baseWidth * state.scale)}px`;
        state.svg.style.height = `${Math.round(state.baseHeight * state.scale)}px`;
        state.svg.style.maxWidth = "none";
        updateScaleLabel(toolbar, state.scale);
    }

    function measureSvg(svg) {
        const viewBox = svg.viewBox && svg.viewBox.baseVal;
        if (viewBox && viewBox.width && viewBox.height) {
            return { width: viewBox.width, height: viewBox.height };
        }

        const bounds = svg.getBoundingClientRect();
        if (bounds.width && bounds.height) {
            return { width: bounds.width, height: bounds.height };
        }

        return { width: 1600, height: 1100 };
    }

    function enhanceSvg(shell, toolbar, state, links) {
        const svg = shell.querySelector("svg");
        if (!svg || svg.dataset.mindmapEnhanced === "true") {
            return;
        }

        svg.dataset.mindmapEnhanced = "true";
        state.svg = svg;

        const dimensions = measureSvg(svg);
        state.baseWidth = dimensions.width;
        state.baseHeight = dimensions.height;

        for (const link of links) {
            const element = findNodeElement(svg, link.id, link.label);
            makeNodeInteractive(element, link.href, link.ariaLabel || link.label);
        }

        applyScale(shell, toolbar, state);
    }

    function setupToolbar(shell, toolbar, state) {
        if (!toolbar) {
            return;
        }

        toolbar.addEventListener("click", function (event) {
            const button = event.target.closest("[data-zoom-action]");
            if (!button) {
                return;
            }

            const action = button.getAttribute("data-zoom-action");
            state.fitMode = false;

            if (action === "out") {
                state.scale -= SCALE_STEP;
            } else if (action === "in") {
                state.scale += SCALE_STEP;
            } else if (action === "reset") {
                state.scale = state.defaultScale;
            } else if (action === "fit") {
                state.fitMode = true;
                state.scale = fitScale(shell, state);
            }

            applyScale(shell, toolbar, state);
        });

        window.addEventListener("resize", function () {
            if (!state.fitMode) {
                return;
            }
            state.scale = fitScale(shell, state);
            applyScale(shell, toolbar, state);
        });
    }

    function initializeMindmap() {
        const shell = document.querySelector(".mindmap-shell");
        const toolbar = document.querySelector(".mindmap-toolbar");
        const linkSource = document.getElementById("mindmap-links");
        if (!shell || !linkSource) {
            return;
        }

        let links = [];
        try {
            links = JSON.parse(linkSource.textContent || "[]");
        } catch (error) {
            console.error("Unable to parse mindmap link metadata.", error);
            return;
        }

        const configuredDefaultScale = Number.parseFloat(shell.dataset.defaultScale || "");
        const state = {
            svg: null,
            baseWidth: 0,
            baseHeight: 0,
            scale: Number.isFinite(configuredDefaultScale) ? configuredDefaultScale : DEFAULT_SCALE,
            defaultScale: Number.isFinite(configuredDefaultScale) ? configuredDefaultScale : DEFAULT_SCALE,
            fitMode: false,
        };

        setupToolbar(shell, toolbar, state);

        const observer = new MutationObserver(function () {
            enhanceSvg(shell, toolbar, state, links);
        });

        observer.observe(shell, { childList: true, subtree: true });
        enhanceSvg(shell, toolbar, state, links);
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initializeMindmap, { once: true });
    } else {
        initializeMindmap();
    }
})();
