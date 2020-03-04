import pytest

from kindergarten_garden import Garden


class TestKindergartenGarden:
    def test_partial_garden_garden_with_single_student(self):
        garden = Garden("RC\nGG")
        assert garden.plants("Alice") == ["Radishes", "Clover", "Grass", "Grass"]

    def test_partial_garden_different_garden_with_single_student(self):
        garden = Garden("VC\nRC")
        assert garden.plants("Alice") == ["Violets", "Clover", "Radishes", "Clover"]

    def test_partial_garden_garden_with_two_students(self):
        garden = Garden("VVCG\nVVRC")
        assert garden.plants("Bob") == ["Clover", "Grass", "Radishes", "Clover"]

    def test_partial_garden_second_student_s_garden(self):
        garden = Garden("VVCCGG\nVVCCGG")
        assert garden.plants("Bob") == ["Clover", "Clover", "Clover", "Clover"]

    def test_partial_garden_third_student_s_garden(self):
        garden = Garden("VVCCGG\nVVCCGG")
        assert garden.plants("Charlie") == ["Grass", "Grass", "Grass", "Grass"]

    def test_full_garden_first_student_s_garden(self):
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        assert garden.plants("Alice"), ["Violets", "Radishes", "Violets", "Radishes"]

    def test_full_garden_second_student_s_garden(self):
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        assert garden.plants("Bob") == ["Clover", "Grass", "Clover", "Clover"]

    def test_full_garden_second_to_last_student_s_garden(self):
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        assert garden.plants("Kincaid") == ["Grass", "Clover", "Clover", "Grass"]

    def test_full_garden_last_student_s_garden(self):
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        assert garden.plants("Larry") == ["Grass", "Violets", "Clover", "Violets"]

    def test_students_are_unordered_first_student(self):
        garden = Garden(
            "VCRRGVRG\nRVGCCGCV", students=["Samantha", "Patricia", "Xander", "Roger"]
        )
        assert garden.plants("Patricia") == ["Violets", "Clover", "Radishes", "Violets"]

    def test_students_are_unordered_last_student(self):
        garden = Garden(
            "VCRRGVRG\nRVGCCGCV", students=["Samantha", "Patricia", "Xander", "Roger"]
        )
        assert garden.plants("Xander") == ["Radishes", "Grass", "Clover", "Violets"]
