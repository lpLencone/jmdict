CREATE TYPE lsource_type AS (
    ls VARCHAR(50),
    ls_lang VARCHAR(5),
    ls_type BOOLEAN, -- True for `full`, False for `part`
    ls_wasei BOOLEAN
);

CREATE TYPE gloss_type AS (
    gl VARCHAR(100),
    g_type VARCHAR(5)
    -- TODO maybe store `g_gend` and `g_lang` (currently no entry uses it)
);
