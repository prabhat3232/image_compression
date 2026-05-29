# Graph Report - .  (2026-05-29)

## Corpus Check
- 100 files · ~50,621 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 421 nodes · 616 edges · 32 communities detected
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 77 edges (avg confidence: 0.79)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Convt Converter Registry|Convt Converter Registry]]
- [[_COMMUNITY_Convt UI and Analytics|Convt UI and Analytics]]
- [[_COMMUNITY_Convt SEO Landing Pages|Convt SEO Landing Pages]]
- [[_COMMUNITY_Browser Local Converters|Browser Local Converters]]
- [[_COMMUNITY_Converter UI Flow|Converter UI Flow]]
- [[_COMMUNITY_E2E Test Specs|E2E Test Specs]]
- [[_COMMUNITY_Test Mocks and Fixtures|Test Mocks and Fixtures]]
- [[_COMMUNITY_PostHog Analytics|PostHog Analytics]]
- [[_COMMUNITY_SEO FAQ Components|SEO FAQ Components]]
- [[_COMMUNITY_Media Tools Flask App|Media Tools Flask App]]
- [[_COMMUNITY_Desktop Runtime Server|Desktop Runtime Server]]
- [[_COMMUNITY_Flask Compression Pipeline|Flask Compression Pipeline]]
- [[_COMMUNITY_UI Select Component|UI Select Component]]
- [[_COMMUNITY_FFmpeg WASM Assets|FFmpeg WASM Assets]]
- [[_COMMUNITY_Playwright Config|Playwright Config]]
- [[_COMMUNITY_Media Test Helpers|Media Test Helpers]]
- [[_COMMUNITY_Production SEO and Ads|Production SEO and Ads]]
- [[_COMMUNITY_Desktop Install Guide|Desktop Install Guide]]
- [[_COMMUNITY_Type Definitions|Type Definitions]]
- [[_COMMUNITY_Archive Converter Tests|Archive Converter Tests]]
- [[_COMMUNITY_Converter Unit Tests|Converter Unit Tests]]
- [[_COMMUNITY_Bun Desktop Entry|Bun Desktop Entry]]
- [[_COMMUNITY_Electrobun Config|Electrobun Config]]
- [[_COMMUNITY_Button Component|Button Component]]
- [[_COMMUNITY_Card Component|Card Component]]
- [[_COMMUNITY_Utils Helpers|Utils Helpers]]
- [[_COMMUNITY_Desktop Download API|Desktop Download API]]
- [[_COMMUNITY_Feature Implementation Docs|Feature Implementation Docs]]
- [[_COMMUNITY_Convt Project Plan|Convt Project Plan]]
- [[_COMMUNITY_Convt README Docs|Convt README Docs]]
- [[_COMMUNITY_Robots and Ads TXT|Robots and Ads TXT]]
- [[_COMMUNITY_Misc Isolated Nodes|Misc Isolated Nodes]]

## God Nodes (most connected - your core abstractions)
1. `DocumentConverter` - 30 edges
2. `getAvailableOutputFormatsFromRegistry()` - 15 edges
3. `getMimeType()` - 14 edges
4. `getFileExtension()` - 13 edges
5. `resolveInputType()` - 13 edges
6. `formatExtension()` - 11 edges
7. `Converter` - 10 edges
8. `ArchiveConverter` - 9 edges
9. `ImageConverter` - 9 edges
10. `capturePostHogEvent()` - 8 edges

## Surprising Connections (you probably didn't know these)
- `Pillow PDF Conversion` --semantically_similar_to--> `img2pdf Lossless PDF`  [INFERRED] [semantically similar]
  brain/project_context.md → filecompress.py
- `Flask App (filecompress.py)` --semantically_similar_to--> `Convt Desktop (Electrobun)`  [INFERRED] [semantically similar]
  filecompress.py → sample/convt/apps/desktop/electrobun.config.ts
- `Image Compressor` --semantically_similar_to--> `Convt Sample Reference App`  [INFERRED] [semantically similar]
  brain/project_context.md → sample/convt/README.md
- `Client-Side Image Editor` --semantically_similar_to--> `Browser-Side Converters`  [INFERRED] [semantically similar]
  templates/index.html → sample/convt/README.md
- `Browser-Side Converters` --semantically_similar_to--> `FFmpeg Processing`  [INFERRED] [semantically similar]
  sample/convt/README.md → brain/project_context.md

## Hyperedges (group relationships)
- **Image Compression Pipeline** — compress_route, batch_processing, quality_validation, output_format_jpg_webp_pdf, zip_multi_download [INFERRED 0.85]
- **SEO Conversion Landing Page** — schema-markup_SchemaMarkup, faq-section_FaqSection, step-guide_StepGuide, why-convert_WhyConvert, format-about_FormatAbout, related-conversions_RelatedConversions, breadcrumbs_Breadcrumbs, last-updated_LastUpdated [INFERRED 0.88]
- **Conversion Analytics Pipeline** — index_Converter, analytics_analytics, analytics_trackEvent, posthog_capturePostHogEvent, posthog_initPostHog [INFERRED 0.90]
- **FFmpeg Media Conversion Stack** — ffmpeg_FFMpegConverter, ffmpeg_getFFmpeg, ffmpeg-assets_getFFmpegAssetUrls, ffmpeg_buildFFmpegStrategies, ffmpeg_preloadFFmpeg [EXTRACTED 0.95]
- **Multi-format converter dispatch** — converters_convert_file, converters_converter_chain, image_image_converter_singleton, types_converter_interface, registry_output_format_resolver [EXTRACTED 0.90]
- **SEO conversion landing page stack** — route_conversion_page, seo_conversion_slug_parser, seo_generate_conversion_head, seo_all_conversions, seo_format_info_record, concept_seo_slug_pattern [EXTRACTED 0.92]
- **Registry–SEO–runtime capability contract** — registry_output_format_resolver, seo_all_conversions, converters_can_convert, test_registry_seo_alignment, test_conversion_integrity_suite [INFERRED 0.88]
- **Media Tools Production Stack** — flask_backend, ffmpeg_processing, docker_deployment, port_3000, uploads_static_volumes [INFERRED 0.80]

## Communities (51 total, 17 thin omitted)

### Community 0 - "Convt Converter Registry"
Cohesion: 0.1
Nodes (32): FormatSelector(), FFmpegConverter, getFFmpeg(), isAudioExtraction(), isFFmpegLoaded(), preloadFFmpeg(), canConvert(), convertFile() (+24 more)

### Community 1 - "Convt UI and Analytics"
Cohesion: 0.05
Nodes (43): ConversionEventProps, analytics, buildProperties, trackEvent, ArchiveConverter, archiveConverter, createZip, extractZip (+35 more)

### Community 2 - "Convt SEO Landing Pages"
Cohesion: 0.09
Nodes (22): ConversionPage(), getFormatPair(), getRelatedConversions(), isValidConversion(), parseConversionSlug(), FaqSection(), getFaqs(), FormatAbout() (+14 more)

### Community 3 - "Browser Local Converters"
Cohesion: 0.05
Nodes (39): Browser-local privacy-first conversion, from-to conversion URL slugs, canConvert, convertFile, Converter dispatch chain, getAvailableOutputFormats, createImageBitmap decode path, ImageConverter (+31 more)

### Community 4 - "Converter UI Flow"
Cohesion: 0.11
Nodes (14): useInstallGuide(), getBatchMode(), getCommonOutputFormats(), getFileEventContext(), getInputMime(), getSelectionContext(), getSourceFormat(), downloadConvertedFile() (+6 more)

### Community 6 - "Test Mocks and Fixtures"
Cohesion: 0.13
Nodes (7): ArchiveConverter, createSimpleDocxFile(), createBinaryMockFile(), ImageDataMock, OffscreenCanvasMock, blobToText(), createMockFile()

### Community 7 - "PostHog Analytics"
Cohesion: 0.19
Nodes (16): buildProperties(), getCurrentPath(), markAnalyticsSessionEntry(), stringifyProps(), trackEvent(), truncateMiddle(), uniqueList(), registerOfflineSupport() (+8 more)

### Community 8 - "SEO FAQ Components"
Cohesion: 0.13
Nodes (17): Client-Side Conversion, FaqSection, Browser Privacy FAQ, getFaqs, isAudioExtraction, FormatAbout, getLastUpdatedISO, SchemaMarkup (+9 more)

### Community 9 - "Media Tools Flask App"
Cohesion: 0.13
Nodes (17): AJAX /compress Endpoint, Media Tools Web App, Browser-Side Converters, Client-Side Image Editor, Convt Logo, Docker Compose Service, Docker Deployment, FFmpeg Processing (+9 more)

### Community 10 - "Desktop Runtime Server"
Cohesion: 0.24
Nodes (9): createAssetFetcher(), findFirstExistingPath(), getDownloadsDir(), getUniqueDownloadPath(), handleDesktopSaveRequest(), resolveBundledPublicDir(), resolveBundledServerEntry(), sanitizeFilename() (+1 more)

### Community 11 - "Flask Compression Pipeline"
Cohesion: 0.22
Nodes (9): Batch File Processing, Filesystem Sync Delay for Chrome, /compress Route, Convt Desktop (Electrobun), Flask App (filecompress.py), / Index Route, Output Formats JPG WEBP PDF, Quality Validation (1-100) (+1 more)

### Community 12 - "UI Select Component"
Cohesion: 0.43
Nodes (6): Select(), SelectContent(), SelectGroup(), SelectItem(), SelectLabel(), SelectValue()

### Community 13 - "FFmpeg WASM Assets"
Cohesion: 0.36
Nodes (5): getAssetBaseUrl(), getDevAssetUrl(), getDevAssetUrls(), getFFmpegAssetUrls(), getLocalAssetUrl()

### Community 16 - "Media Test Helpers"
Cohesion: 0.6
Nodes (3): createTestAudio(), createTestVideo(), ensureTestDir()

### Community 19 - "Production SEO and Ads"
Cohesion: 0.5
Nodes (4): compress.dsnmsolutions.com, Google AdSense, Google Analytics, OG Image (Media Tools)

## Knowledge Gaps
- **71 isolated node(s):** `/ Index Route`, `/download_file Route`, `Quality Validation (1-100)`, `Output Formats JPG WEBP PDF`, `Filesystem Sync Delay for Chrome` (+66 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **17 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `getMimeType()` connect `Convt Converter Registry` to `Convt SEO Landing Pages`, `E2E Test Specs`, `Test Mocks and Fixtures`, `Playwright Config`, `Offline PWA Support`?**
  _High betweenness centrality (0.059) - this node is a cross-community bridge._
- **Why does `getAvailableOutputFormatsFromRegistry()` connect `Convt Converter Registry` to `Convt SEO Landing Pages`?**
  _High betweenness centrality (0.054) - this node is a cross-community bridge._
- **Why does `DocumentConverter` connect `E2E Test Specs` to `Convt Converter Registry`, `Test Mocks and Fixtures`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `getAvailableOutputFormatsFromRegistry()` (e.g. with `.canConvert()` and `getAvailableOutputFormats()`) actually correct?**
  _`getAvailableOutputFormatsFromRegistry()` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `getMimeType()` (e.g. with `.getMimeTypeForExtractedFile()` and `.convert()`) actually correct?**
  _`getMimeType()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 6 inferred relationships involving `getFileExtension()` (e.g. with `getSourceFormat()` and `.getMimeTypeForExtractedFile()`) actually correct?**
  _`getFileExtension()` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `resolveInputType()` (e.g. with `.getDocumentKind()` and `convertFile()`) actually correct?**
  _`resolveInputType()` has 8 INFERRED edges - model-reasoned connections that need verification._