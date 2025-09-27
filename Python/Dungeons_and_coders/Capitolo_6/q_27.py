'''
Valuti la purezza dei cristalli. Applica `grade(score)` con le soglie: `A` (>=90), `B` (>=80), `C` (>=70), `D` (>=60), altrimenti `F`. Mantieni la firma e titola i test.
'''

def grade(score: int) -> str:
    
    match score:
        case score if score >= 90:
            return 'A'
        case score if score >= 80:
            return 'B'
        case score if score >= 70:
            return 'C'
        case score if score >= 60:
            return 'D'
        case _:
            return 'F'