ChangeLog
---------

* 2016-04-06  1.7.0
    - Finished documentation.
    - Utility methods from `germanium.util.*` that need germanium, are
      postfixed with `_g` so they don't conflict with `germanium.static.*`
    - `wait` exported also in `germanium.static`

* 2016-04-05  1.6.13
    - Fixed tests to close HttpServer.
    - Chrome is now part of the test matrix.
    - Documentation.
    - pyp different deployments for 2.7, and 3.5 using different distributions.
    - 100% coverage JS Locator and selector.
    - Removed simple locator.

* 2016-04-02  1.6.12  Python 2.7 tests all pass. Implemented `without_children` for selectors. Better error reporting.
* 2016-04-01  1.6.11  Fixed `bdist_wheel` release for Python 2.7.
* 2016-04-01  1.6.10  Bugfixes. Chrome tests. Selectors can return `element`, `element_list`, `exists`, `not_exists`, and callable.
* 2016-03-22  1.6.9  Bugfixes. `inside`/`contains` on selectors. Multiple selectors support.
* 2016-03-22  1.6.8  Bugfixes. Check for element arrays in `js`, `wait` on multiple functions, `locators` as `selectors`.
* 2016-03-21  1.6.7  `only_visible` filtering by default. Selenium 2.53.1 support. `not_exists` check for deferred locators.
* 2016-03-18  1.6.6  Test matrix runs end-to-end tests for all python versions.
* 2016-03-17  1.6.5  Selenium:2.52.0. `TableRow` selectors. Test matrix across python versions.
* 2016-03-15  1.6.4  `Element` selector can search for attribute content parts.
* 2016-03-14  1.6.3  `Element` selector. IE8/9 Full test coverage.
* 2016-03-11  1.6.2  Removed LOG to console. Fixes IE.
* 2016-03-08  1.6.1  Added `get_attributes`. Fixed pip setup fail (Issue #1).
* 2016-03-07  1.6.0  Tests run now through the static API. Started working on documentation.
* 2016-03-04  1.5.1  Added JsLocator, and made `Text()` not use the simple locator.
* 2016-03-03  1.5.0  Added positional filtering for selectors. `Link('edit').right_of(Text('User 11'))`
* 2016-02-22  1.4.1  Added a bunch of static API calls. Better tests.
* 2016-02-16  1.4.0  Added initial selectors support. Started work on a static API.
* 2016-02-11  1.3.10  *BugFix* Fixed the wrapper JS so it gives the `arguments` of the function down.
* 2016-02-11  1.3.9  *BugFix* pass extra parameters in `execute_script` or `get` webdriver calls.
* 2016-02-11  1.3.8  setup.py trying to get the long description in.
* 2016-02-11  1.3.7  Renamed README so it should appear in Pypy hopefully.
* 2016-02-11  1.3.6  Added multikey typing: `type_keys(g, '<ctrl-left*3>')`
* 2016-02-03  1.3.5  Added `germanium.js()`. Added documentation.
* 2016-01-28  1.3.4  *BugFix* Detect if the node is an element, by nodeType and not instanceof. (Fixes Chrome issues)
* 2016-01-26  1.3.3  *BugFix* Fixed the `type_keys` implementation for IE.
* 2016-01-25  1.3.2  *BugFix* `S` locator doesn't throw when is not finding elements.
* 2016-01-25  1.3.1  *BugFix* Release script.
* 2016-01-25  1.3.0  Added `S` super locator.
* 2016-01-25  1.2.0  Added `wait` utility function. Added a bunch of tests.
* 2015-12-03  1.1.1  Fixed returning `dict` object instead of `WebElement` under python 3.4.
* 2015-11-30  1.1.0  Added `type_keys` API.
* 2015-11-30  1.0.1  PIP deployment fix for python 3.4.

