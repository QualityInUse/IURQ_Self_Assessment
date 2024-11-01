import pytest

from iu_rq_self_assessment_bot.MainTask.PDFModule.PDFChecker import _countSentences, _countWords, _countReferences


def test_countSentences():
    text = ('The head, or the spherical body part that contains the brain and rests at the top of the human body, '
            'has quite a few individual organs and body parts on it. (It should quickly be mentioned that hair '
            'occupies the space on top of the head, and the ears, the organs responsible for hearing, are located '
            'on either side of the head.) From top to bottom, the eyebrows, or horizontal strips of hair that can '
            'be found above the eye, are the first components of the head. The eyes are below them, and are round, '
            'orb-like organs that allow humans to see.')

    assert _countSentences(text) == 4


def test_countWords():
    text = ('The head, or the spherical body part that contains the brain and rests at the top of the human body, '
            'has quite a few individual organs and body parts on it. (It should quickly be mentioned that hair '
            'occupies the space on top of the head, and the ears, the organs responsible for hearing, are located '
            'on either side of the head.) From top to bottom, the eyebrows, or horizontal strips of hair that can '
            'be found above the eye, are the first components of the head. The eyes are below them, and are round, '
            'orb-like organs that allow humans to see.')

    assert _countWords(text) == 102


def test_countReferences():
    text = ('The head, or the spherical [1, p. 12] body part that contains the brain and rests at the top of the human'
            ' body, has quite a few individual organs and body parts on it [2, pp. 33-34]. (It should quickly be '
            'mentioned that hair occupies the space on top of the head, and the ears [2, pp. 4], the organs '
            'responsible for hearing, are located on either side of the head.) From top to bottom, the eyebrows, '
            'or horizontal strips of hair that can be found above the eye, are the first components of the '
            'head [1, p. 34-33]. The eyes are below them, and are round, orb-like organs that allow humans '
            'to see [3, p. 4].')

    assert _countReferences(text) == 3
