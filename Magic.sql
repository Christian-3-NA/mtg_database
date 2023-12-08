/*Sassy Solitaire Skeletons: Christian Anderson, Dominic Macias, Nina Martinez-Alvarez
Project Phase III: Magic the Gathering Database
*/

-- Table for Card
CREATE TABLE Card (
    card_id INT,
    card_name VARCHAR(100) NOT NULL,
    card_set VARCHAR(50),
    card_text VARCHAR(500),
    PRIMARY KEY (card_id) 
);

-- Table for Collection
CREATE TABLE Collection (
    collection_id INT,
    c_cards_owned INT,
    num_cards INT,
    FOREIGN KEY (c_cards_owned) REFERENCES Card(card_id),
    PRIMARY KEY (collection_id)
);

-- Table for Deck
CREATE TABLE Deck (
    deck_id INT,
    deck_name VARCHAR(100) NOT NULL,
    tags VARCHAR(50),
    format VARCHAR(50),
    d_cards_owned INT,
    FOREIGN KEY (d_cards_owned) REFERENCES Card(card_id),
    PRIMARY KEY (deck_id)
);

-- Table for Profile
CREATE TABLE Profile (
    user_id INT,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    decks_owned INT,
    paired_collection INT,
    FOREIGN KEY (paired_collection) REFERENCES Collection(collection_id),
    FOREIGN KEY (decks_owned) REFERENCES Deck(deck_id),
    PRIMARY KEY (user_id)
);

-- Table for Admin
CREATE TABLE Admin (
    admin_id INT,
    PRIMARY KEY (admin_id)
);

-- Table for Card Library
CREATE TABLE CardLibrary (
    library_id INT,
    manager_id INT,
    l_cards_owned INT,
    FOREIGN KEY (l_cards_owned) REFERENCES Card(card_id),
    FOREIGN KEY (manager_id) REFERENCES Admin(admin_id),
    PRIMARY KEY (library_id)
);

-- Filling with some default/sample info
INSERT Into Admin(admin_id)
Values(0);

INSERT Into Card(card_id, card_name, card_set, card_text)
Values(1, 'Acrobatic Leap', 'The Lost Caverns Of Ixalan', 'Target creature gets +1/+3 and gains flying until end of turn. Untap it.');
INSERT Into Card(card_id, card_name, card_set, card_text)
Values(2, 'Cosmium Blast', 'The Lost Caverns Of Ixalan', 'Cosmium Blast deals 4 damage to target attacking or blocking creature.');

INSERT Into Collection(collection_id, c_cards_owned, num_cards)
Values(1, 1, 1);
INSERT Into Collection(collection_id, c_cards_owned, num_cards)
Values(2, 2, 2);

INSERT Into Deck(deck_id, deck_name, tags, format, d_cards_owned)
Values(1, 'Test', 'unfinished', 'Combo', 2);

INSERT Into Profile(user_id, password, email, decks_owned, paired_collection)
Values(1, 'pass12345', 'nsmzk3@umsystem.edu', 1, 1);

INSERT Into CardLibrary(library_id, manager_id, l_cards_owned)
Values(1, 0, 1);
INSERT Into CardLibrary(library_id, manager_id, l_cards_owned)
Values(2, 0, 2);

