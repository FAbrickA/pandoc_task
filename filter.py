import sys
import panflute

headers = dict()


def upper_str(elem, doc):
    if isinstance(elem, panflute.Str):
        elem.text = elem.text.upper()


def my_filter(elem, doc):
    # header warning
    if isinstance(elem, panflute.Header):
        text = panflute.stringify(elem)
        if text in headers.keys():  # if repeated
            if not headers[text]:  # if we didn't warn about this text
                sys.stderr.write(f"Header repeated: \"{text}\"")
                headers[text] = True
        else:
            headers[text] = False

    # bold text
    if isinstance(elem, panflute.Str) and elem.text.lower() == "bold":
        return panflute.Strong(elem)

    # header to upper
    if isinstance(elem, panflute.Header) and elem.level <= 3:
        return elem.walk(upper_str)


def main(doc=None):
    return panflute.run_filter(my_filter, doc=doc)


if __name__ == "__main__":
    main()
