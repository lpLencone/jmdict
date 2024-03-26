from config import load_config
from lxml import etree

import db
import xml.etree.ElementTree as ET


def print_elements(element, indent=0):
    print('    ' * indent + element.tag)
    for child in element:
        print_elements(child, indent + 1)

tree = etree.parse('JMdict_e')
root = tree.getroot()

entries = root.findall('.//entry')

for entry in entries: 
    e = dict()
    e['ent_seq'] = entry.find('./ent_seq').text
    print(e['ent_seq'], end=': ')
    e['k_ele'] = list()

    for k_ele in entry.findall('./k_ele'):
        k = dict()
        k['keb'] = k_ele.find('./keb').text
        print(k['keb'], end=' , ')

        k['ke_inf'] = [inf.text for inf in 
                       k_ele.findall('./ke_inf')]
        if k['ke_inf']: print(k['ke_inf'], end=' , ')

        k['ke_pri'] = [pri.text for pri in 
                       k_ele.findall('./ke_pri')]
        if k['ke_pri']: print(k['ke_pri'], end=' , ')

    for r_ele in entry.findall('./r_ele'):
        r = dict()
        r['reb'] = r_ele.find('./reb').text
        print(r['reb'], end=' , ')

        r['re_nokanji'] = r_ele.find('./re_nokanji')

        r['re_restr'] = [restr.text for restr in 
                         r_ele.findall('./re_restr')]
        if r['re_restr']: print(r['re_restr'], end=' , ')

        r['re_inf'] = [inf.text for inf in 
                       r_ele.findall('./re_inf')]
        if r['re_inf']: print(r['re_inf'], end=' , ')

        r['re_pri'] = [pri.text for pri in 
                       r_ele.findall('./re_pri')]
        if r['re_pri']: print(r['re_pri'], end=' , ')

    for sense in entry.findall('./sense'):
        s = dict()
        
        s['stagk'] = [stagk.text for stagk in
                      sense.findall('./stagk')]
        if s['stagk']: print(s['stagk'], end=' , ')

        s['stagr'] = [stagr.text for stagr in
                      sense.findall('./stagr')]
        if s['stagr']: print(s['stagr'], end=' , ')

        s['pos'] = [pos.text for pos in
                    sense.findall('./pos')]
        if s['pos']: print(s['pos'], end=' , ')

        s['field'] = [field.text for field in
                      sense.findall('./field')]
        if s['field']: print(s['field'], end=' , ')
        print(etree.tostring(

        s['misc'] = [misc.text for misc in
                      sense.findall('./misc')]
        if s['misc']: print(s['misc'], end=' , ')

        s['lsource'] = dict()
        for lsource in sense.findall('./lsource'):
            s['lsource']['ls'] = lsource.text
            print(etree.tostring(lsource))
            print(lsource.text)
            if lsource.attrib:
                exit()

        
        

    print()
