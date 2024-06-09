CREATE DATABASE JokesDB;

USE JokesDB;

CREATE TABLE jokes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    joke TEXT NOT NULL , 
    category VARCHAR(50) NOT NULL
);

-- Insert Dad Jokes
INSERT INTO jokes (joke, category) VALUES
('Why don’t skeletons fight each other? They don’t have the guts.', 'Dad jokes'),
('What do you call fake spaghetti? An impasta.', 'Dad jokes'),
('I would avoid the sushi if I was you. It’s a little fishy.', 'Dad jokes');

-- Insert Sports Jokes
INSERT INTO jokes (joke, category) VALUES
('Why was the basketball court wet? Because the players kept dribbling on it.', 'Sports Jokes'),
('Why did the golfer bring two pairs of pants? In case he got a hole in one.', 'Sports Jokes'),
('Why did the football team go to the bank? To get their quarterback.', 'Sports Jokes');

-- Insert Knock Knock Jokes
INSERT INTO jokes (joke, category) VALUES
('Knock, knock. Who’s there? Lettuce. Lettuce who? Lettuce in, it’s cold out here!', 'Knock Knock Jokes'),
('Knock, knock. Who’s there? Cow says. Cow says who? No, cow says mooooo!', 'Knock Knock Jokes'),
('Knock, knock. Who’s there? Atch. Atch who? Bless you!', 'Knock Knock Jokes');

-- Repeat inserts until you reach 500 entries
