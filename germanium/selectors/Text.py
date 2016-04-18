from .AbstractSelector import AbstractSelector


class Text(AbstractSelector):
    """
    Just a selector that finds the text in the page.
    """
    def __init__(self, text):
        super(Text, self).__init__()
        self._text = text

    def get_selectors(self):
        """ Return a JS selector to find the text """
        js_selector = """js:
            var searchedText = "%s";

            function text(node) {
                return node.innerText || node.textContent || "";
            }

            if (text(document.body).indexOf(searchedText) < 0) {
                return null;
            }

            var processing_queue = [ document.body ];
            var result = [];

            while (processing_queue.length) {
                var foundChildElement = false;
                var currentNode = processing_queue.splice(0, 1)[0];

                for (var i = 0; i < currentNode.children.length; i++) {
                    if (text(currentNode.children[i]).indexOf(searchedText) >= 0) {
                        foundChildElement = true;
                        processing_queue.push(currentNode.children[i]);
                    }
                }

                if (!foundChildElement) {
                    result.push(currentNode);
                }
            }

            return result;
        """ % str(self._text).replace('"', '\\"', 100000)

        return [js_selector]
