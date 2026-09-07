<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## communication
- primary_language: en-AU
- audience: Expanded 2026 delegates in Linz — XR artists, interactive-art practitioners and critical-heritage researchers, comfortable with real-time engines and capture pipelines and interested in how the work is made
- objective: In ten presenter-led minutes show the artwork before theorising it, defend the layered-provenance position that separates speculative co-creation from appropriation, explain the dual-platform and capture decisions well enough to be reused, and state the boundary of the findings, so that delegates can repeat the recognition-versus-attachment caution and the dual-platform model
- core_message: A heritage site can be reimagined as a postgeographic sanctuary — a living counter-archive co-created with the community it serves — and the pairing of a high-fidelity contemplative world with a low-barrier co-creative one is the transferable part
- consumption_mode: presentation

## mode
- mode: custom
- mode_references: showcase, instructional
- mode_behavior: Lead with the work itself at full visual scale for two pages so the audience has something to hold, then alternate — each conceptual or technical page states one idea and decomposes it into its parts step by step, with an image page resetting the rhythm between the harder blocks; close by naming the three registers of contribution and the limit of what the findings support.

## visual_style
- visual_style: custom
- visual_style_references: swiss-minimal, photo-editorial
- visual_style_behavior: The same grid-locked white field and hairline discipline as its companion deck, but photography leads — the garden renders run full-bleed or to a hard page edge on the image pages, with type set on a solid QUT-blue plate or clear white margin rather than over the picture; text pages stay austere and two- or three-column with a short QUT-blue rule under the title, and no image is ever tinted or overlaid with a scrim.

## colors
- background: #FFFFFF
- secondary_bg: #F2F5F8
- primary: #003562
- accent: #0091DA
- secondary_accent: #8A8D8F
- body_text: #1A1A1A
- secondary_text: #5A6570
- divider: #D8DFE6
- surface: #F2F5F8
- grid: #E8EDF2

## typography
- font_family: Calibri, sans-serif
- title_family: Georgia, serif
- body_family: Calibri, sans-serif
- display_family: Georgia, serif
- display: 72
- data: 56
- title: 48
- subtitle: 36
- lead: 34
- body: 28
- annotation: 22
- footnote: 16

## icons
- library: tabler-filled
- inventory: tabler-filled/home, tabler-filled/map-pin, tabler-filled/user, tabler-filled/world, tabler-filled/mountain, tabler-filled/headphones, tabler-filled/microphone, tabler-filled/clock-hour-3, tabler-filled/message, tabler-filled/photo, tabler-filled/database, tabler-filled/archive, tabler-filled/device-desktop, tabler-filled/plane, tabler-filled/bulb, tabler-filled/compass, tabler-filled/chart-dots-2, tabler-filled/sparkles

## images
- vr-garden-hero: images/vr_garden_hero.png | source=user | crop=adaptive
- vr-detail-blossom-path: images/vr_detail_blossom_path.png | source=user | crop=adaptive
- vr-dusk-lantern: images/vr_dusk_lantern.png | source=user | crop=adaptive
- vr-borrowed-hills: images/vr_borrowed_hills.png | source=user | crop=adaptive
- minecraft-ai-guide: images/minecraft_ai_guide.png | source=user | crop=no-crop
- qut-logo-white: images/qut_logo_white.png | source=user | crop=no-crop
- sketchfab-archive: images/sketchfab_archive.png | source=user | crop=no-crop
- scan-lidar-onsite: images/scan_lidar_onsite.jpg | source=user | crop=adaptive

## page_visualizations
- P05: chart/dumbbell_chart
- P09: chart/treemap_chart

## page_rhythm
- P01: anchor
- P02: breathing
- P03: dense
- P04: breathing
- P05: dense
- P06: dense
- P07: breathing
- P08: dense
- P09: dense
- P10: dense
- P11: anchor

## pptx_structure
- mode: flat

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters
- 图片用我自己的，如果还需要加其他照片，注明就好我后期自己加 (user)
