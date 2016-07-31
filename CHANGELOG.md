ChangeLog
---------

* 2016-08-01  1.9.1
    - Added `use_window` to permit selecting the active window that we're working with.

    _Bugfixes_

    - Added `inside`/`containing`/`containing_all` checks for empty nodes, so `Element("div").containing(Text("missing")) will return empty, instead of all the divs.
    - Throw meaningful error messages if the property is not defined on the Germanium/WebDriver instance.

* 2016-07-29  1.9.0
    - Completely rewrote `inside`/`containing`/`without_elements` as filters. This extends from only XPath selectors that can be used as filters to _any_ kind of selector (CSS, JS, or custom `AbstractSelector` class).
    - Added `containing_all` to match elements that contain all the given selectors.
    - Documentation updates.

    _Bugfixes_
    - Positional filtering sorting fixes, now preffering elements that overlap.
    - XPath `Element` indexes, if they happen also on nested elements using `containing`, works as expected.

* 2016-07-25  1.8.3
    _Bugfixes_

    - Sort the elements vertically/horizontally on the positional filtering.

* 2016-07-19  1.8.2
    - Rewrote the positional filtering. Blazing fast.

* 2016-07-12  1.8.1
    - Updated documentation.
    - Python upgrades: 3.5.2, 3.4.5, 2.7.12
    - Allow space separated CSS classes in the `Element` locator.

    _Bugfixes_

    - Don't die when WebDriver returns `None` instead of empty list.

* 2016-07-06  1.8.0
    - Firefox 47.0.1 support.
    - selenium 2.52.6 support.
    - Allow instantiation of Firefox with or without marionette.
    - Use drivers that are already packed in the `germaniumdrivers`.

* 2016-06-14  1.7.14
    - Firefox 46 support.
    - selenium 2.52.4 support.
    - `file_select()` renamed to `select_file()`.
    - Documentation update.

* 2016-06-10  1.7.13
    - New function `file_select()` allows selecting the file to be uploaded into a file input.
    - `InputFile` selector added.

* 2016-06-06  1.7.12
    - New function `parent_node()` allows getting the parent node of an element (selector).
    - New function `child_nodes(only_elements=True)` allows getting the child nodes/elements of a parent element (selector).
    - Tests refactoring to call _"open the browser"_ instead of the misleading _"open firefox"_, when not actually running firefox.
    - Updated the documentation.

* 2016-06-02  1.7.11
    - `wait()` now also takes into account the closure times for timeouts.
    - Documentation updates.
    - Minor cleanup on the default test.

* 2016-05-29  1.7.10
    - Added more tests on the behavior of Selenium.
    - Use Ubuntu 16.04 as a base for docker images.
    - Bugfixes for alerts support in Chrome 51.

* 2016-05-19  1.7.9
    - `iframe_selector` can be changed on the Germanium instance while the instance still runs.

* 2016-05-09  1.7.8
    - `germanium.util.Color` supports now also `rgba()` values.

    _Bugfixes_

    - Fixed bug in `get_style()` to return the actual style even when the style is set from JS.
    - #4 Fixed bug in `highlight()` for multiple simultaneous highlights.
    - #8 Fixed Xpath expression calculated invalid.

* 2016-04-28  1.7.7
    - `get_style` function implemented, to get a single CSS property value
    - `element_list(x)` allows the first parameter as index, to get only an element.
    - `germanium.util.Color` utility class to parse and compare classes.

* 2016-04-26  1.7.6
    - selenium 2.52.2 support.
    - Better ordering for finding elements positionally.
    - #7 Allow custom XPath into Elements.
    - #6 index values in Element should also allow string values.

* 2016-04-21  1.7.5
    - #3 inside/containing filter support now also CSS on AbstractSelector, not only XPath.

* 2016-04-19  1.7.4
    - Added `get_text` support function to get the text from selectors.
    - Added `highlight` utility function, to aid debugging of tests.

    _Bugfixes_

    - `get_attributes` can return now the attributes also for invisible elements.
    - #2 Extra check if WebDriver returns single elements.

* 2016-04-17  1.7.3
    - Added select support (combo boxes), with `select` and `deselect` functions.
    - Added `get_value` to get the value(s) of selectors.
    - Callable support in reference selectors (e.g. `.inside(callable)`).

    _Bugfixes_

    - Updated documentation.

* 2016-04-15  1.7.2
    - Added alert support, including `Alert` selector, locator, and `type_keys` integration.
    - IE8 is now part of the test matrix.

* 2016-04-10  1.7.1
    - Added `text()` function to selectors and locators.
    - Added `drag_and_drop()`.

    _Bugfixes_

    - Added timeouts for `wait_for_..`
    - Minor cleanups.
    - Updated documentation.

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
* 2016-03-22  1.6.9  Bugfixes. `inside`/`containing` on selectors. Multiple selectors support.
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

