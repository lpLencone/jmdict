CREATE TABLE IF NOT EXISTS entry (
    id INT NOT NULL, -- not auto-generated; each entry comes with
                     -- a predefined `ent_seq` identifier
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS k_ele (
    id INT GENERATED ALWAYS AS IDENTITY,
    entry_id INT NOT NULL,

    keb VARCHAR(20) NOT NULL,
    ke_inf VARCHAR(6)[],
    ke_pri VARCHAR(10)[],

    PRIMARY KEY (id),

    CONSTRAINT fk_entry
        FOREIGN KEY (entry_id)
            REFERENCES entry(id)
);

CREATE TABLE IF NOT EXISTS r_ele (
    id INT GENERATED ALWAYS AS IDENTITY,
    entry_id INT NOT NULL,

    reb VARCHAR(20) NOT NULL,
    re_nokanji VARCHAR(10),
    re_restr VARCHAR(20),
    re_inf VARCHAR(6)[],
    re_pri VARCHAR(10)[],

    PRIMARY KEY (id),

    CONSTRAINT fk_entry
        FOREIGN KEY (entry_id)
            REFERENCES entry(id)
);

CREATE TABLE IF NOT EXISTS sense (
    id INT GENERATED ALWAYS AS IDENTITY,
    entry_id INT NOT NULL,

    stagk INT[], -- references k_ele
    stagr INT[], -- references r_ele
    pos VARCHAR(15)[],
    -- TODO maybe store `xref` and `ant`
    field VARCHAR(15)[],
    misc VARCHAR(15)[],

    lsource lsource_type[], -- see create-types.sql
    -- lsource VARCHAR(50)[],
    -- ls_lang VARCHAR(5),
    -- ls_type VARCHAR(5),
    -- ls_wasei VARCHAR(1),
    
    dial VARCHAR(15)[],

    gloss VARCHAR(100)[] NOT NULL, -- even though it's marked with an asterisk (*), the 
                                   -- documentation says there'll be at least one for 
                                   -- each sense tag
    g_lang VARCHAR(5),
    -- TODO maybe store `g_gend` (currently no entry uses it)
    g_type VARCHAR(5),
    
    -- TODO maybe store `pri`
    s_inf VARCHAR(100)[], 

    PRIMARY KEY (id),

    CONSTRAINT fk_entry
        FOREIGN KEY (entry_id)
            REFERENCES entry(id)
);
