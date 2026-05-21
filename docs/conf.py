# *******************************************************************************
# Copyright (c) 2025 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0
#
# SPDX-License-Identifier: Apache-2.0
# *******************************************************************************

project = "S-CORE Infrastructure"
project_url = "https://eclipse-score.github.io/infrastructure"
version = "0.1"

extensions = [
    "score_sphinx_bundle",
]

# Enable cross-reference resolution for [text](file.md#anchor) links up to h4.
# Without this, MyST treats heading anchors as opaque and cannot resolve them.
myst_heading_anchors = 4

# MyST's default slug function keeps leading digits (GitHub-style: "33-toolchain-management"),
# but docutils strips them ("toolchain-management"). Since Sphinx section IDs use docutils,
# the two disagree and cross-references break. Aligning on make_id fixes this.
myst_heading_slug_func = "docutils.nodes.make_id"

html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_js_files = ["js/mindmap.js"]
