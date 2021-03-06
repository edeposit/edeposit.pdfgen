#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# !!! DO NOT EDIT THIS FILE!!!
# !!! THIS IS AUTOMATICALLY GENERATED FILE !!!
# !!! SEE requests_template.py AND requests_generator.py FOR DETAILS !!!
#
# Imports =====================================================================
import textwrap
from collections import namedtuple
from collections import OrderedDict


# Constants ===================================================================
MAX_LINK_SIZE = 83
NONE_VAL = "Nezvoleno"


# Functions & classes =========================================================
class GenerateContract(namedtuple("GenerateContract", ["firma",
                                                       "pravni_forma",
                                                       "sidlo",
                                                       "ic",
                                                       "dic",
                                                       "zastoupen"])):
    """
    Request to generate contract.

    Attributes:
        firma (str): As it is defined in contract.
        pravni_forma (str): As it is defined in contract.
        sidlo (str): As it is defined in contract.
        ic (str): As it is defined in contract.
        dic (str): As it is defined in contract.
        zastoupen (str): As it is defined in contract.
    """
    pass


#
# !!! DO NOT EDIT THIS FILE!!!
# !!! THIS IS AUTOMATICALLY GENERATED FILE !!!
# !!! SEE requests_template.py AND requests_generator.py FOR DETAILS !!!
#
class GenerateReview(namedtuple("GenerateReview", ['nazev',
                                                   'podnazev',
                                                   'cast',
                                                   'nazev_casti',
                                                   'isbn',
                                                   'isbn_souboru_publikaci',
                                                   'generated_isbn',
                                                   'author1',
                                                   'author2',
                                                   'author3',
                                                   'poradi_vydani',
                                                   'misto_vydani',
                                                   'rok_vydani',
                                                   'nakladatel_vydavatel',
                                                   'vydano_v_koedici_s',
                                                   'cena',
                                                   'anotace',
                                                   'libraries_accessing',
                                                   'libraries_that_can_access',
                                                   'is_public',
                                                   'url',
                                                   'offer_to_riv',
                                                   'category_for_riv',
                                                   'zpracovatel_zaznamu',
                                                   'format',
                                                   'filename',
                                                   'internal_url'])):
    """
    Generate review of sent form.

    Attributes:
        nazev (any): Název ePublikace
        podnazev (any): Podnázev
        cast (any): Část (svazek,díl)
        nazev_casti (any): Název části, dílu
        isbn (any): ISBN
        isbn_souboru_publikaci (any): ISBN souboru
        generated_isbn (any): Přidělit ISBN
        author1 (any): Autor
        author2 (any): Autor 2
        author3 (any): Autor 3
        poradi_vydani (any): Pořadí vydání, verze
        misto_vydani (any): Místo vydání
        rok_vydani (any): Rok vydání
        nakladatel_vydavatel (any): Nakladatel
        vydano_v_koedici_s (any): Vydáno v koedici s
        cena (any): Cena v Kč
        anotace (any): Anotace knihy
        libraries_accessing (any): Oprávnění knihovnám
        libraries_that_can_access (any): Seznam knihoven
        is_public (any): Vystavení na volném internetu
        url (any): URL
        offer_to_riv (any): Zpřístupnit pro RIV
        category_for_riv (any): Seznam oborů pro RIV
        zpracovatel_zaznamu (any): Zpracovatel záznamu
        format (any): Formát souboru
        filename (any): Název souboru
        internal_url (any): Edeposit URL
    """
    def get_rst(self):
        # this is used to maintain order of informations
        semantic_dict = OrderedDict([
            ["nazev", "Název ePublikace"],
            ["podnazev", "Podnázev"],
            ["cast", "Část (svazek,díl)"],
            ["nazev_casti", "Název části, dílu"],
            ["isbn", "ISBN"],
            ["isbn_souboru_publikaci", "ISBN souboru"],
            ["generated_isbn", "Přidělit ISBN"],
            ["author1", "Autor"],
            ["author2", "Autor 2"],
            ["author3", "Autor 3"],
            ["poradi_vydani", "Pořadí vydání, verze"],
            ["misto_vydani", "Místo vydání"],
            ["rok_vydani", "Rok vydání"],
            ["nakladatel_vydavatel", "Nakladatel"],
            ["vydano_v_koedici_s", "Vydáno v koedici s"],
            ["cena", "Cena v Kč"],
            ["anotace", "Anotace knihy"],
            ["libraries_accessing", "Oprávnění knihovnám"],
            ["libraries_that_can_access", "Seznam knihoven"],
            ["is_public", "Vystavení na volném internetu"],
            ["url", "URL"],
            ["offer_to_riv", "Zpřístupnit pro RIV"],
            ["category_for_riv", "Seznam oborů pro RIV"],
            ["zpracovatel_zaznamu", "Zpracovatel záznamu"],
            ["format", "Formát souboru"],
            ["filename", "Název souboru"],
            ["internal_url", "Edeposit URL"],
        ])

        rst = ""
        for key, description in semantic_dict.items():
            content = getattr(self, key)

            # human intepretation of python's internal values
            if isinstance(content, basestring):
                try:
                    content = content.encode("utf-8")
                except UnicodeDecodeError:
                    pass
            elif isinstance(content, bool):
                content = "Ano" if content else "Ne"
            elif content is None:
                content = NONE_VAL
            elif isinstance(content, list):
                tmp = []
                for item in content:
                    if "title" in item:
                        try:
                            tmp.append(item["title"].encode("utf-8"))
                        except UnicodeDecodeError:
                            tmp.append(item["title"])
                    else:
                        tmp.append(str(item))
                content = ", ".join(tmp)

            description = description.strip()
            content = str(content).strip()

            if not content.strip():
                content = NONE_VAL

            if content != NONE_VAL and key in ["url", "internal_url"]:
                content = self.wrap_long_links(content)
            else:
                content = self.escape_rst_sequences(content)

            rst += ":%s: %s\n" % (description, content)

        return str(rst)

    def wrap_long_links(self, s):
        if len(s) < MAX_LINK_SIZE:
            return s

        url = s.strip()
        enchanced = [
            "`%s <%s>`_" % (url_part, url)
            for url_part in textwrap.wrap(s, MAX_LINK_SIZE)
        ]

        return " ".join(enchanced)

    def escape_rst_sequences(self, s):
        out = ""
        for char in s:
            if ord(char) < 128 and char not in [" ", "\t", "\n"]:
                out += "\\"

            out += char

        return out
#
# !!! DO NOT EDIT THIS FILE!!!
# !!! THIS IS AUTOMATICALLY GENERATED FILE !!!
# !!! SEE requests_template.py AND requests_generator.py FOR DETAILS !!!
#


class RST2PDF(namedtuple("RST2PDF", ["rst_content",
                                     "style",
                                     "header",
                                     "footer"])):
    """
    Generic request to convert RST file to PDF.

    Attributes:
        rst_content (str): Content of the generated PDF file.
        style (str): Style for the generated PDF file.
        header (str, default None): Header of each page.
        footer (str, default pagecount): Footer of each page.
    """
    def __new__(self, rst_content, style, header=None, footer=None):
        return super(RST2PDF, self).__new__(
            self,
            rst_content,
            style,
            header,
            footer
        )
