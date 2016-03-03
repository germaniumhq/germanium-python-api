germanium
=========

Germanium is a set of extensions on top of the regular WebDriver API, allowing
for a super easy creation of tests. It's opensource and free.

Simply put Germanium is a Web Testing API that doesn't suck.

Here is some draft documentation: https://github.com/bmustiata/germanium/blob/master/doc/api/index.adoc

ChangeLog
---------

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

