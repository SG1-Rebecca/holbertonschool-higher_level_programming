#!/usr/bin/python3
import os.path
import logging

PLACEHOLDERS = ["name", "event_title", "event_date", "event_location"]


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template
    with placeholders and a list of objects
    """
    # Check input type
    if not isinstance(template, str):
        logging.error("Input template must be a string")
        return

    if not isinstance(attendees, list) or not all(isinstance(person, dict) for person in attendees):
        logging.error("Attendees must be a list of dictionaries")
        return

    # Handle Empty input
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

# Process Each attendeee
    attendees_index = 1

    for attendee in attendees:
        fill_template = template

        for placeholder in PLACEHOLDERS:
            value = attendee.get(placeholder)

            if value is None:
                value = "N/A"

            fill_template = fill_template.replace("{" + placeholder + "}", str(value))

        # Generate output file
        output_filename = f"output_{attendees_index}.txt"

        # Write file
        try:
            with open(output_filename, "w") as outfile:
                outfile.write(fill_template)
            logging.info(f"Generated {output_filename}")
        except IOError as error:
            logging.error(f"Failed to write {output_filename}: {error}")

        attendees_index += 1


if __name__ == "__main__":
    try:
        with open('template.txt', 'r') as file:
            template_content = file.read()
    except FileNotFoundError:
        logging.error("Template file 'template.txt' not found")
        template_content = ""
    except Exception as e:
        logging.error(f"Error reading template file: {e}")
        template_content = ""

    # List of attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Call the function with the template and attendees list
    generate_invitations(template_content, attendees)
