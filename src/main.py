from config import load_config
from lxml import etree

import db
import config
import xml.etree.ElementTree as ET
import json

tree = etree.parse('JMdict_e')

jmdict = dict()

# # Already in the database
# entities = tree.docinfo.internalDTD.entities()
# entities = [(e.name, e.content) for e in entities]

root = tree.getroot()
entries = root.findall('.//entry')

jmdict['entry'] = list()
for entry in entries: 
    e = dict()
    e['ent_seq'] = entry.find('./ent_seq').text
    e['k_ele'] = list()

    for k_ele in entry.findall('./k_ele'):
        k = dict()
        k['keb'] = k_ele.find('./keb').text

        k['ke_inf'] = [inf.text for inf in 
                       k_ele.findall('./ke_inf')]

        e['k_ele'].append(k)

    e['r_ele'] = list()
    for r_ele in entry.findall('./r_ele'):
        r = dict()
        r['reb'] = r_ele.find('./reb').text

        r['re_nokanji'] = r_ele.find('./re_nokanji')
        r['re_nokanji'] = r['re_nokanji'] is not None

        r['re_restr'] = [restr.text for restr in 
                         r_ele.findall('./re_restr')]

        r['re_inf'] = [inf.text for inf in 
                       r_ele.findall('./re_inf')]

        e['r_ele'].append(r)

    e['sense'] = list()
    for sense in entry.findall('./sense'):
        s = dict()
        
        s['stagk'] = [stagk.text for stagk in
                      sense.findall('./stagk')]

        s['stagr'] = [stagr.text for stagr in
                      sense.findall('./stagr')]

        s['pos'] = [pos.text for pos in
                    sense.findall('./pos')]

        s['field'] = [field.text for field in
                      sense.findall('./field')]

        s['misc'] = [misc.text for misc in
                      sense.findall('./misc')]

        s['lsource'] = list()
        for lsource in sense.findall('./lsource'):
            l = dict()
            l['ls'] = lsource.text
            l['ls_lang'] = lsource.get('{http://www.w3.org/XML/1998/namespace}lang', None)
            l['ls_type'] = lsource.get('ls_type', None)
            l['ls_wasei'] = lsource.get('ls_wasei', None)

            s['lsource'].append(l)

        s['dial'] = [dial.text for dial in
                     sense.findall('./dial')]

        s['gloss'] = list()
        for gloss in sense.findall('./gloss'):
            g = dict()
            g['gl'] = gloss.text
            g['g_type'] = gloss.get('g_type', None)
            s['gloss'].append(g)

        
        s['s_inf'] = [inf.text for inf in
                      sense.findall('./s_inf')]

        e['sense'].append(s)

    jmdict['entry'].append(e)


config = load_config()
db.populate_entries(config, jmdict['entry'])
