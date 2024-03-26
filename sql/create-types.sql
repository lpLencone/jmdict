CREATE TYPE lsource_type AS (
    ls VARCHAR(50),
    ls_lang VARCHAR(5),
    ls_type BOOLEAN, -- True for `full`, False for `part`
    ls_wasei BOOLEAN
);
