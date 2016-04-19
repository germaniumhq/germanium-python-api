
def _is_displayed_filter(item):
    try:
        return item.is_displayed()
    except Exception:
        return False
