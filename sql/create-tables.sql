CREATE TABLE IF NOT EXISTS entity (
    id INT GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(15) UNIQUE NOT NULL,
    description VARCHAR(80) UNIQUE NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS entry (
    id INT NOT NULL, -- not auto-generated; each entry comes with
                     -- a predefined `ent_seq` identifier
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS k_ele (
    id INT GENERATED ALWAYS AS IDENTITY,
    entry_id INT NOT NULL,

    keb VARCHAR(30) NOT NULL,
    ke_inf INT[], -- references entity

    PRIMARY KEY (id),

    CONSTRAINT fk_entry
        FOREIGN KEY (entry_id)
            REFERENCES entry(id)
);

CREATE TABLE IF NOT EXISTS r_ele (
    id INT GENERATED ALWAYS AS IDENTITY,
    entry_id INT NOT NULL,

    reb VARCHAR(50) NOT NULL, -- There are some bigger than 30 AFAIK
    re_nokanji BOOLEAN,
    re_restr VARCHAR(20)[],
    re_inf INT[], -- references entity

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
    pos INT[], -- references entity
    field INT[], -- references entity
    misc INT[], -- references entity
    -- TODO maybe store `xref` and `ant`

    lsource lsource_type[], -- see create-types.sql
    
    dial INT[], -- references entity

    gloss gloss_type[] NOT NULL, -- even though it's marked with an asterisk (*), the 
                                   -- documentation says there'll be at least one for 
                                   -- each sense tag
    
    -- TODO maybe store `pri`
    s_inf VARCHAR(100)[], 

    PRIMARY KEY (id),

    CONSTRAINT fk_entry
        FOREIGN KEY (entry_id)
            REFERENCES entry(id)
);
