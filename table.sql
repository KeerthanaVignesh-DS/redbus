CREATE TABLE bus_routes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    route_name TEXT NOT NULL,
    route_link TEXT NOT NULL,
    busname TEXT NOT NULL,
    bustype TEXT NOT NULL,
    departing_time TIME NOT NULL,
    duration TEXT NOT NULL,
    reaching_time TIME NOT NULL,
    star_rating FLOAT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    seats_available INT NOT NULL
);
