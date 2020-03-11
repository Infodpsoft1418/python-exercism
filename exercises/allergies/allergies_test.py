import pytest

from allergies import Allergies


class TestAllergies:
    def test_eggs_not_allergic_to_anything(self):
        assert not Allergies(0).allergic_to("eggs")

    def test_allergic_only_to_eggs(self):
        assert Allergies(1).allergic_to("eggs")

    def test_allergic_to_eggs_and_something_else(self):
        assert Allergies(3).allergic_to("eggs")

    def test_allergic_to_something_but_not_eggs(self):
        assert not (Allergies(2).allergic_to("eggs"))

    def test_eggs_allergic_to_everything(self):
        assert Allergies(255).allergic_to("eggs")

    def test_peanuts_not_allergic_to_anything(self):
        assert not (Allergies(0).allergic_to("peanuts"))

    def test_allergic_only_to_peanuts(self):
        assert Allergies(2).allergic_to("peanuts")

    def test_allergic_to_peanuts_and_something_else(self):
        assert Allergies(7).allergic_to("peanuts")

    def test_allergic_to_something_but_not_peanuts(self):
        assert not (Allergies(5).allergic_to("peanuts"))

    def test_peanuts_allergic_to_everything(self):
        assert Allergies(255).allergic_to("peanuts")

    def test_shellfish_not_allergic_to_anything(self):
        assert not (Allergies(0).allergic_to("shellfish"))

    def test_allergic_only_to_shellfish(self):
        assert Allergies(4).allergic_to("shellfish")

    def test_allergic_to_shellfish_and_something_else(self):
        assert Allergies(14).allergic_to("shellfish")

    def test_allergic_to_something_but_not_shellfish(self):
        assert not (Allergies(10).allergic_to("shellfish"))

    def test_shellfish_allergic_to_everything(self):
        assert Allergies(255).allergic_to("shellfish")

    def test_strawberries_not_allergic_to_anything(self):
        assert not (Allergies(0).allergic_to("strawberries"))

    def test_allergic_only_to_strawberries(self):
        assert Allergies(8).allergic_to("strawberries")

    def test_allergic_to_strawberries_and_something_else(self):
        assert Allergies(28).allergic_to("strawberries")

    def test_allergic_to_something_but_not_strawberries(self):
        assert not (Allergies(20).allergic_to("strawberries"))

    def test_strawberries_allergic_to_everything(self):
        assert Allergies(255).allergic_to("strawberries")

    def test_tomatoes_not_allergic_to_anything(self):
        assert not (Allergies(0).allergic_to("tomatoes"))

    def test_allergic_only_to_tomatoes(self):
        assert Allergies(16).allergic_to("tomatoes")

    def test_allergic_to_tomatoes_and_something_else(self):
        assert Allergies(56).allergic_to("tomatoes")

    def test_allergic_to_something_but_not_tomatoes(self):
        assert not (Allergies(40).allergic_to("tomatoes"))

    def test_tomatoes_allergic_to_everything(self):
        assert Allergies(255).allergic_to("tomatoes")

    def test_chocolate_not_allergic_to_anything(self):
        assert not (Allergies(0).allergic_to("chocolate"))

    def test_allergic_only_to_chocolate(self):
        assert Allergies(32).allergic_to("chocolate")

    def test_allergic_to_chocolate_and_something_else(self):
        assert Allergies(112).allergic_to("chocolate")

    def test_allergic_to_something_but_not_chocolate(self):
        assert not (Allergies(80).allergic_to("chocolate"))

    def test_chocolate_allergic_to_everything(self):
        assert Allergies(255).allergic_to("chocolate")

    def test_pollen_not_allergic_to_anything(self):
        assert not Allergies(0).allergic_to("pollen")

    def test_allergic_only_to_pollen(self):
        assert Allergies(64).allergic_to("pollen")

    def test_allergic_to_pollen_and_something_else(self):
        assert Allergies(224).allergic_to("pollen")

    def test_allergic_to_something_but_not_pollen(self):
        assert not Allergies(160).allergic_to("pollen")

    def test_pollen_allergic_to_everything(self):
        assert Allergies(255).allergic_to("pollen")

    def test_cats_not_allergic_to_anything(self):
        assert not (Allergies(0).allergic_to("cats"))

    def test_allergic_only_to_cats(self):
        assert Allergies(128).allergic_to("cats")

    def test_allergic_to_cats_and_something_else(self):
        assert Allergies(192).allergic_to("cats")

    def test_allergic_to_something_but_not_cats(self):
        assert not (Allergies(64).allergic_to("cats"))

    def test_cats_allergic_to_everything(self):
        assert Allergies(255).allergic_to("cats")

    def test_no_allergies(self):
        assert Allergies(0).lst == []

    def test_just_eggs(self):
        assert Allergies(1).lst == ["eggs"]

    def test_just_peanuts(self):
        assert Allergies(2).lst == ["peanuts"]

    def test_just_strawberries(self):
        assert Allergies(8).lst == ["strawberries"]

    def test_eggs_and_peanuts(self):
        assert Allergies(3).lst == ["eggs", "peanuts"]

    def test_more_than_eggs_but_not_peanuts(self):
        assert Allergies(5).lst == ["eggs", "shellfish"]

    def test_lots_of_stuff(self):
        assert Allergies(248).lst == [
            "strawberries",
            "tomatoes",
            "chocolate",
            "pollen",
            "cats",
        ]

    def test_everything(self):
        assert (
            Allergies(255).lst
            == [
                "eggs",
                "peanuts",
                "shellfish",
                "strawberries",
                "tomatoes",
                "chocolate",
                "pollen",
                "cats",
            ],
        )

    def test_no_allergen_score_parts(self):
        assert Allergies(509).lst == [
            "eggs",
            "shellfish",
            "strawberries",
            "tomatoes",
            "chocolate",
            "pollen",
            "cats",
        ]
