class Student:
    
    def __init__(self, full_name, section, spanish_grade, english_grade,social_studies_grade,science_grade):
        
        self.full_name=full_name
        self.section=section
        self.spanish_grade=spanish_grade
        self.english_grade=english_grade
        self.social_studies_grade=social_studies_grade
        self.science_grade=science_grade
    
    def to_dict(self):
        
        return {
            'Full_name':self.full_name,
            'Section':self.section,
            'Spanish_grade':self.spanish_grade,
            'English_grade':self.english_grade,
            'Social_studies_grade':self.social_studies_grade,
            'Science_grade':self.science_grade
        }