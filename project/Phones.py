
CREATE TABLE materials (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    points INTEGER NOT NULL
);
INSERT INTO materials (name, points) VALUES
('Copper', 5),
('Gold', 10),
('Titanium', 100),
('Silver', 50);
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('materials.db')
cursor = conn.cursor()

def calculate_total_points(materials):
    total_points = 0
    for material in materials:
        cursor.execute("SELECT points FROM materials WHERE name=?", (material,))
        result = cursor.fetchone()
        if result:
            total_points += result[0]
    return total_points

if __name__ == "__main__":
    # Input materials as a list
    input_materials = ['Copper', 'Gold', 'Titanium', 'Silver']

    # Calculate total points
    total_points = calculate_total_points(input_materials)

    print(f"Total Points: {total_points}")

# Close the database connection
conn.close()
