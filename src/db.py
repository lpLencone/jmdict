import psycopg2
import json

def connect(config):
    try:
        with psycopg2.connect(**config) as conn:
            return conn
    except (pgycopg2.DatabaseError, Exception) as error:
        print(error)   


def populate_jmdict_entities(config, entities):

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.executemany("""
                    INSERT INTO entity(name, description)
                    VALUES(%s, %s)
                """, entities)

                conn.commit()

    except (psycopg2.DatabaseError, Exception) as e:
        print(e)
    

def populate_entries(config, entries):

    def create_sql_for_k_ele(k_ele, entry_id, cur):
        ke_inf = [(inf, ) for inf in k_ele['ke_inf']]

        inf_id = list()
        for inf in ke_inf:
            cur.execute("""
                SELECT id FROM entity
                WHERE entity.description = %s;
            """, inf)
            inf_id.append(cur.fetchone()[0])

        insert_into = 'INSERT INTO k_ele (entry_id, keb'
        values = "VALUES (%s, '%s'" % (entry_id, k_ele['keb'])
        if inf_id:
            insert_into += ', %s' % 'ke_inf'
            values += ', ARRAY [%s]' % ', '.join(map(str, inf_id))

        insert_into += ') '
        values += ');'
        return insert_into + values

    def create_sql_for_r_ele(r_ele, entry_id, cur):
        re_inf = [(inf, ) for inf in r_ele['re_inf']]

        inf_id = list()
        for inf in re_inf:
            cur.execute("""
                SELECT id FROM entity
                WHERE entity.description = %s;
            """, inf)
            inf_id.append(cur.fetchone()[0])

        insert_into = 'INSERT INTO r_ele (entry_id, reb, re_nokanji'
        values = "VALUES (%s, '%s', %s" % (entry_id, r_ele['reb'], r_ele['re_nokanji'])

        if r_ele['re_restr']:
            insert_into += ', re_restr'
            values += ", ARRAY ['%s" % "', '".join(r_ele['re_restr']) + "']"

        if inf_id:
            insert_into += ', %s' % 're_inf'
            values += ', ARRAY [%s]' % ', '.join(map(str, inf_id))

        insert_into += ') '
        values += ');'
        return insert_into + values

    # # Just raise the goddamn exception lol
    # try:
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            for entry in entries:
                entry_id = entry['ent_seq']

                cur.execute("""
                        INSERT INTO entry (id)
                        VALUES (%s)
                        ON CONFLICT (id) DO NOTHING
                """, (entry_id,))

                for k_ele in entry['k_ele']:
                    sql = create_sql_for_k_ele(k_ele, entry_id, cur)
                    print(sql)
                    cur.execute(sql)

                for r_ele in entry['r_ele']:
                    sql = create_sql_for_r_ele(r_ele, entry_id, cur)
                    print(sql)
                    cur.execute(sql)

            conn.commit()

    # except (psycopg2.DatabaseError, Exception) as e:
    #     print(e)
