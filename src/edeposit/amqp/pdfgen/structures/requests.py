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
from collections import namedtuple, OrderedDict


# Functions & classes =========================================================
class GenerateContract(namedtuple("GenerateContract", ["firma",
                                                       "pravni_forma",
                                                       "sidlo",
                                                       "ic",
                                                       "dic",
                                                       "zastoupen",
                                                       "jednajici"])):
    """
    Request to generate contract.

    Attributes:
        firma (str): As it is defined in contract.
        pravni_forma (str): As it is defined in contract.
        sidlo (str): As it is defined in contract.
        ic (str): As it is defined in contract.
        dic (str): As it is defined in contract.
        zastoupen (str): As it is defined in contract.
        jednajici (str): As it is defined in contract.
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
                                                   'offer_to_riv',
                                                   'category_for_riv',
                                                   'is_public',
                                                   'libraries_accessing',
                                                   'libraries_that_can_access',
                                                   'zpracovatel_zaznamu',
                                                   'url',
                                                   'format',
                                                   'filename'])):
    """
    Generate review of sent form.

    Attributes:
        nazev (any): Název
        podnazev (any): Podnázev
        cast (any): Část
        nazev_casti (any): Název části
        isbn (any): ISBN
        isbn_souboru_publikaci (any): ISBN souboru
        generated_isbn (any): Přidělit ISBN
        author1 (any, default None): Autor
        author2 (any, default None): Autor 2
        author3 (any, default None): Autor 3
        poradi_vydani (any): Pořadí
        misto_vydani (any): Místo vydání
        rok_vydani (any): Rok vydání
        nakladatel_vydavatel (any): Nakladatel
        vydano_v_koedici_s (any): Vydáno v koedici s
        cena (any): Cena v Kč
        offer_to_riv (any): Zpřístupnit pro RIV
        category_for_riv (any): Kategorie pro RIV
        is_public (any): Veřejná publikace
        libraries_accessing (any): Oprávnění knihovnám
        libraries_that_can_access (any): Seznam knihoven
        zpracovatel_zaznamu (any): Zpracovatel záznamu
        url (any): URL
        format (any): Formát souboru
        filename (any): Název souboru
    """
    def __new__(self,
                nazev,
                podnazev,
                cast,
                nazev_casti,
                isbn,
                isbn_souboru_publikaci,
                generated_isbn,
                poradi_vydani,
                misto_vydani,
                rok_vydani,
                nakladatel_vydavatel,
                vydano_v_koedici_s,
                cena,
                offer_to_riv,
                category_for_riv,
                is_public,
                libraries_accessing,
                libraries_that_can_access,
                zpracovatel_zaznamu,
                url,
                format,
                filename,
                author1=None,
                author2=None,
                author3=None):
        return super(GenerateReview, self).__new__(
            self,
            nazev,
            podnazev,
            cast,
            nazev_casti,
            isbn,
            isbn_souboru_publikaci,
            generated_isbn,
            author1,
            author2,
            author3,
            poradi_vydani,
            misto_vydani,
            rok_vydani,
            nakladatel_vydavatel,
            vydano_v_koedici_s,
            cena,
            offer_to_riv,
            category_for_riv,
            is_public,
            libraries_accessing,
            libraries_that_can_access,
            zpracovatel_zaznamu,
            url,
            format,
            filename
        )

    def get_rst(self):
        semantic_dict = OrderedDict([
            ["nazev", "Název"],
            ["podnazev", "Podnázev"],
            ["cast", "Část"],
            ["nazev_casti", "Název části"],
            ["isbn", "ISBN"],
            ["isbn_souboru_publikaci", "ISBN souboru"],
            ["generated_isbn", "Přidělit ISBN"],
            ["author1", "Autor"],
            ["author2", "Autor 2"],
            ["author3", "Autor 3"],
            ["poradi_vydani", "Pořadí"],
            ["misto_vydani", "Místo vydání"],
            ["rok_vydani", "Rok vydání"],
            ["nakladatel_vydavatel", "Nakladatel"],
            ["vydano_v_koedici_s", "Vydáno v koedici s"],
            ["cena", "Cena v Kč"],
            ["offer_to_riv", "Zpřístupnit pro RIV"],
            ["category_for_riv", "Kategorie pro RIV"],
            ["is_public", "Veřejná publikace"],
            ["libraries_accessing", "Oprávnění knihovnám"],
            ["libraries_that_can_access", "Seznam knihoven"],
            ["zpracovatel_zaznamu", "Zpracovatel záznamu"],
            ["url", "URL"],
            ["format", "Formát souboru"],
            ["filename", "Název souboru"],
        ])

        rst = ""
        for key, val in semantic_dict.items():
            key = getattr(self, key)

            # human intepretation of python's internal values
            if isinstance(key, basestring):
                key = key.encode("utf-8")
            elif isinstance(key, bool):
                key = "Ano" if key else "Ne"
            elif key is None:
                key = "Nezvoleno"
            elif isinstance(key, list):
                tmp = []
                for item in key:
                    if "title" in item:
                        tmp.append(item["title"].encode("utf-8"))
                    else:
                        tmp.append(str(item))
                key = ", ".join(tmp)

            val = val.strip()
            rst += ":%s: %s\n" % (val, str(key).strip())

        return str(rst)
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
