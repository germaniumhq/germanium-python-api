//noinspection JSAnnotator,JSReferencingArgumentsOutsideOfFunction,JSUnresolvedVariable,ThisExpressionReferencesGlobalObjectJS
return (function() {
  var rootNode = arguments[0] || document.body;
  var searchedText = arguments[1];
  var checkFunction = arguments[2] ? exact : contains; // exactMatch
  var processText = arguments[3] ? trim : noop; // trimText

  /*
   * text - returns the text of the given DOM node.
   * @param {Element} node The node to extract the text
   * @return {string}
   */
  function text(node) {
      return node.innerText || node.textContent || "";
  }

  /**
   * trim - Trims the given text.
   * @param {string} text
   * @return {string}
   */
  function trim(text) {
      return text.replace(/^\s+|\s+$/gm,'');
  }

  /**
   * noop - Keeps the text intact.
   * @param {string} text
   * @return {string}
   */
  function noop(text) {
      return text;
  }

  /**
   * contains - Checkes if the haystack string contains the needle.
   * @param {string} haystack
   * @param {string} needle
   * @return {boolean}
   */
  function contains(haystack, needle) {
      return haystack.indexOf(needle) >= 0;
  }

  /**
   * equals - Checks if the strings are equal.
   * @param {string} value1
   * @param {string} value2
   * @return {boolean}
   */
  function exact(value1, value2) {
      return value1 == value2;
  }

  // no point in searching if it's not there.
  if (!contains(text(rootNode), searchedText)) {
      return null;
  }

  var processing_queue = [ rootNode ];
  var result = [];

  while (processing_queue.length) {
      var foundChildElement = false;
      var currentNode = processing_queue.splice(0, 1)[0];

      for (var i = 0; i < currentNode.children.length; i++) {
          if (checkFunction(processText(text(currentNode.children[i])), searchedText)) {
              foundChildElement = true;
              processing_queue.push(currentNode.children[i]);
          }
      }

      if (!foundChildElement) {
          result.push(currentNode);
      }
  }

  return result;
}.apply(this, arguments));

