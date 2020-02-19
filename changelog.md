# Changelog

All notable changes to this package will be documented in this file.

## [Unreleased]

## [0.1.3] - 2019-02-18

### Added

- Possibility to add nested lists to your list objects
- Added "inherit" styling option to list items which makes the list item take all the styling of it's parent
- Added possibility for list items to be just sentences instead of objects, if the dev chooses the sentence option it will
  automatically inherit the styling of the parent.

### Removed

- Remove empty sections from CHANGELOG, they occupy too much space and
  create too much noise in the file. People will have to assume that the
  missing sections were intentionally left out because they contained no
  notable changes.

## [0.1.2] - 2019-02-16

### Added

- Instead of sending an object to the UI class to add content you can now send just a string this way "styling|slow|type|text"
- Your sentences can now be entire paragraphs the class will proceed to slice it into sentences that fit the UI
- You can now center-left your content in styling
- Added lists to the types available for the dev
- Added styling option underline wich adds a line below the content stylized.

## [0.1.1] - 2019-02-15

### Added

- You can now choose to adjust the size of the UI to the content or leave it to the predefined height.
- Added styling possibilities to the sentences in the UI (newline, upper, lower, centered)
- Added possibility to display content in the UI character by character

## 0.1.0 - 2019-02-14

### Added
- Possibility to choose type of display of the UI (centered, bordered, fixed)
- Possibility to add sentences to the ui by sending an object to the UI class

[unreleased]: https://github.com/olivierlacan/keep-a-changelog/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/olivierlacan/keep-a-changelog/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.3.0...v1.0.0
[0.3.0]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.8...v0.1.0
[0.0.8]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.7...v0.0.8
[0.0.7]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.6...v0.0.7
[0.0.6]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.5...v0.0.6
[0.0.5]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.4...v0.0.5
[0.0.4]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/olivierlacan/keep-a-changelog/releases/tag/v0.0.1
