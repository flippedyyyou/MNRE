relation_classes = {
    "part_of": """
class PartOf(Relation):
    \"\"\"
    Description: Represents a relationship where one entity is a part of, or component within, another entity.
    Examples: (Circle Undone, Arkham Horror LCG), (engine, car), (chapter, book), (keyboard, computer), (branch, tree)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """,
    
    "peer": """
class Peer(Relation):
    \"\"\"
    Description: Represents a relationship where two entities are of similar type or status and are considered as equals or counterparts in a certain context.
    Examples: (Microsoft, Apple), (dogs, wolves), (chess, checkers), (Democrats, Republicans), (France, Germany), (Facebook, Twitter)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """,

    "member_of": """
class MemberOf(Relation):
    \"\"\"
    Description: Represents a relationship where an entity is a member of an organization, group, or collection.
    Examples: (John Doe, Chess Club), (France, United Nations), (Doctor, Medical Association), (Apple Inc., Technology Consortium), (Frodo Baggins, Fellowship of the Ring)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """,
    
    "contain": """
class Contain(Relation):
    \"\"\"
    Description: Represents a relationship where one entity physically or conceptually contains another.
    Examples: (Bottle, Water), (Library, Books), (United States, California), (Folder, Document), (Ocean, Fish), (Galaxy, Solar System)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """,
    
    "present_in": """
class PresentIn(Relation):
    \"\"\"
    Description: Indicates that an entity is present in or part of a location or setting.
    Examples: (Oxygen, Air), (Audience, Theater), (Artifacts, Museum), (Soldiers, Battlefield), (Students, Classroom)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """,
    
    "locate_at": """
class LocateAt(Relation):
    \"\"\"
    Description: Specifies the physical or conceptual location of an entity at a specific site.
    Examples: (Eiffel Tower, Paris), (Statue of Liberty, New York City), (Ancient Ruins, Rome), (Concert, Madison Square Garden), (Olympic Games, Tokyo)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """,
    
    "place_of_residence": """
class PlaceOfResidence(Relation):
    \"\"\"
    Description: Indicates the place where an individual or group lives or resides.
    Examples: (Albert Einstein, Princeton), (Hermit Crab, Shell), (Queen Elizabeth II, Buckingham Palace), (Penguins, Antarctica), (Nomadic Tribes, Deserts)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """,

    "held_on": """
class HeldOn(Relation):
    \"\"\"
    Description: Specifies the date or time on which an event or occurrence is held or takes place.
    Examples: (World Cup, 2022), (Olympics, 2024), (Product Launch, April 2023), (Concert, Friday night), (Graduation Ceremony, June 5)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """,

    "subsidiary": """
class Subsidiary(Relation):
    \"\"\"
    Description: Represents a relationship where one company is owned or controlled by another company.
    Examples: (YouTube, Google), (Instagram, Meta), (Whole Foods, Amazon), (Merrill Lynch, Bank of America), (LinkedIn, Microsoft)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """,

    "alternate_names": """
class AlternateNames(Relation):
    \"\"\"
    Description: Indicates alternative names or aliases that an entity may go by.
    Examples: (J.K. Rowling, Robert Galbraith), (New York City, Big Apple), (Beijing, Peking), (William, Bill), (Automobile, Car)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """,

    "couple": """
class Couple(Relation):
    \"\"\"
    Description: Represents a romantic or marital relationship between two people.
    Examples: (John Lennon, Yoko Ono), (Barack Obama, Michelle Obama), (Romeo, Juliet), (David Beckham, Victoria Beckham), (Prince Harry, Meghan Markle)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """,

    "nationality": """
class Nationality(Relation):
    \"\"\"
    Description: Specifies the country of nationality or citizenship of an individual.
    Examples: (Albert Einstein, German), (Salma Hayek, Mexican), (Adele, British), (Shakira, Colombian), (Leonardo da Vinci, Italian)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """,

    "place_of_birth": """
class PlaceOfBirth(Relation):
    \"\"\"
    Description: Indicates the location where an individual was born.
    Examples: (Leonardo DiCaprio, Los Angeles), (Albert Einstein, Ulm), (Queen Elizabeth II, London), (Elon Musk, Pretoria), (Freddie Mercury, Zanzibar)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """,

    "awarded": """
class Awarded(Relation):
    \"\"\"
    Description: Indicates that an entity has received a specific award or honor.
    Examples: (Albert Einstein, Nobel Prize), (Beyoncé, Grammy), (J.K. Rowling, Hugo Award), (Steve Jobs, National Medal of Technology), (Barack Obama, Nobel Peace Prize)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """,

    "charges": """
class Charges(Relation):
    \"\"\"
    Description: Represents criminal or legal charges brought against an individual.
    Examples: (Al Capone, Tax Evasion), (Martha Stewart, Insider Trading), (Socrates, Corrupting the Youth), (Joan of Arc, Heresy), (Nelson Mandela, Sabotage)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """,

    "parent": """
class Parent(Relation):
    \"\"\"
    Description: Indicates a parental relationship, where one person is the parent of another.
    Examples: (Mary, Jesus), (George Washington, Mary Ball Washington), (Queen Elizabeth II, Prince Charles), (Barack Obama Sr., Barack Obama), (John Lennon, Sean Lennon)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """,

    "siblings":"""
class Siblings(Relation):
    \"\"\"
    Description: Represents a sibling relationship between two people.
    Examples: (Liam Hemsworth, Chris Hemsworth), (Mary, Martha), (Serena Williams, Venus Williams), (George, Fred Weasley), (Luke Skywalker, Leia Organa)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """,

    "neighbor":"""
class Neighbor(Relation):
    \"\"\"
    Description: Indicates neighboring geographical or spatial proximity between entities.
    Examples: (United States, Canada), (France, Germany), (Apartment A, Apartment B), (House 1, House 2), (City Park, Museum)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """,

    "alumni":"""
class Alumni(Relation):
    \"\"\"
    Description: Specifies that an individual has graduated from or attended a specific educational institution.
    Examples: (Steve Jobs, Reed College), (Barack Obama, Harvard), (Emma Watson, Brown University), (Mark Zuckerberg, Harvard), (Bill Gates, Harvard)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """,

    "religion": """
class Religion(Relation):
    \"\"\"
    Description: Indicates the religious affiliation of an individual.
    Examples: (Mahatma Gandhi, Hinduism), (Dalai Lama, Buddhism), (Queen Elizabeth II, Anglicanism), (Martin Luther King Jr., Christianity), (Albert Einstein, Judaism)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """,

    "race": """
class Race(Relation):
    \"\"\"
    Description: Specifies the racial background of an individual.
    Examples: (Malcolm X, African American), (Freddie Mercury, Parsi), (Albert Einstein, Ashkenazi Jew), (Tiger Woods, African American-Thai), (Bruce Lee, Chinese)
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        super().__init__(head_entity = head_entity, tail_entity = tail_entity)
    """
}

