def isMatchExtensions(path, extensions):
    """
    -- input --------------
    path :
        pathlib.path.
    extensions :
        list[str].
    -- output --------------
    void
    """
    return path.suffix in extensions