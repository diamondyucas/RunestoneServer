# *************************************
# |docname| - assignment-related tables
# *************************************

db.define_table(
    "assignments",
    Field("course", db.courses),
    Field("name", "string"),
    Field(
        "points", "integer", default=0, notnull=True
    ),  # max possible points on the assignment, cached sum of assignment_question points
    Field(
        "threshold_pct", "float"
    ),  # threshold required to qualify for maximum points on the assignment; null means use actual points
    Field("released", "boolean"),
    Field(
        "allow_self_autograde", "boolean"
    ),  # if True, when student clicks to autograde assignment, it calculates totals; otherwise it only scores individual questions but doesn't calculate score for the assignment
    Field("description", "text"),
    Field("duedate", "datetime"),
    Field("enforce_due", "boolean"),
    Field("visible", "boolean"),
    Field("is_timed", "boolean", default=False),
    Field("time_limit", "integer"),
    Field("from_source", "boolean"),
    Field("nofeedback", "boolean"),
    Field("nopause", "boolean"),
    format="%(name)s",
    migrate=table_migrate_prefix + "assignments.table",
)


db.define_table(
    "grades",
    # This table records grades on whole assignments, not individual questions
    Field("auth_user", db.auth_user),
    Field("assignment", db.assignments),
    Field("score", "double"),
    Field("manual_total", "boolean"),
    Field("projected", "double"),
    # guid for the student x assignment cell in the external gradebook
    #
    # Guessing that the ``lis_outcome_url`` length is actually inteded for this field, use that as its maximum length.
    Field("lis_result_sourcedid", "string", length=1024),
    # web service endpoint where you send signed xml messages to insert into gradebook; guid above will be one parameter you send in that xml; the actual grade and comment will be others
    #
    # Per the `LTI spec v1.1.1 <https://www.imsglobal.org/specs/ltiv1p1p1/implementation-guide>`_ in section 6, the maximum length of the ``lis_outcome_url`` field is 1023 characters.
    Field("lis_outcome_url", "string", length=1024),
<<<<<<< HEAD
    Field("is_submitted", "string"),
=======
    Field("is_submit", "string"),
>>>>>>> b5a4e0424297a1be3a5fae2f49a03faa076538bd
    migrate=table_migrate_prefix + "grades.table",
)

db.define_table(
    "practice_grades",
    Field("auth_user", db.auth_user),
    Field("course_name", "string"),
    Field("score", "double"),
    Field("lis_result_sourcedid", "string"),
    # guid for the student x assignment cell in the external gradebook
    Field("lis_outcome_url", "string"),
    # web service endpoint where you send signed xml messages to insert into gradebook; guid above will be one parameter you send in that xml; the actual grade and comment will be others
    migrate=table_migrate_prefix + "practice_grades.table",
)


# .. _question_grades table:
#
# question_grades
# ===============
db.define_table(
    "question_grades",
    # This table records grades on individual gradeable items
    Field("sid", type="string", notnull=True),
    Field("course_name", type="string", notnull=True),
    Field("div_id", type="string", notnull=True),
    # The ID of a record in the answer table (mchoice_answers, fitb_answers, etc.) that was graded.
    Field("answer_id", type="integer"),
    Field("deadline", "datetime"),
    Field("score", type="double"),
    Field("comment", type="text"),
    migrate=table_migrate_prefix + "question_grades.table",
)
