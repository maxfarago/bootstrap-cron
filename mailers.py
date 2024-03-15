from datetime import datetime, timedelta

from log import logger
from db import get_cxn, close_cxn


def attendance():
    # initial DB connection to get all event data
    try:
        cxn = get_cxn()
        cur = cxn.cursor()
        query = "SELECT * FROM public.event;"
        cur.execute(query)
        all_events = cur.fetchall()
    except Exception as e:
        logger.error(e)
        return False
    finally:
        close_cxn()

    # filter down to only current events (happening today)
    today = datetime.today().strftime("%a %d %b %Y")
    current_events = []
    for id, name, start, end in all_events:
        # get time diff between start and end dates
        # to create a list of all the event dates
        delta = end - start
        event_dates = [
            (start + timedelta(days=i)).strftime("%a %d %b %Y")
            for i in range(delta.days)
        ]
        if today in event_dates:
            event = {"id": id, "name": name}
            current_events.append(event)

        logger.debug(f"Event {name} with ID {id} has {len(event_dates)} days")

    # new DB connection to get enrollees for current events
    current_event_ids = [event["id"] for event in current_events]
    try:
        cxn = get_cxn()
        cur = cxn.cursor()
        query = f"""
            SELECT event_id, CONCAT(name_first, ' ', name_last)
            FROM enrollment
            JOIN public.user ON enrollment.user_id = public.user.id
            WHERE event_id = ANY(ARRAY{current_event_ids})
            AND is_enrolled = TRUE
        """
        cur.execute(query)
        all_enrollees = cur.fetchall()
    except Exception as e:
        logger.error(e)
        return False
    finally:
        close_cxn()

    # for now, loop through the current events
    # and just log the list of enrollees to stdout
    for event in current_events:
        logger.debug(f"EVENT: {event['name']}")
        event_enrollees = [
            enrollee[1] for enrollee in all_enrollees if enrollee[0] == event["id"]
        ]
        for enrollee in event_enrollees:
            logger.debug(f"- {enrollee}")

    return True
