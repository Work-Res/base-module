NOT_APPLICABLE = "N/A"
OPEN = "open"
CLOSED = "closed"

APPLICATION_STATUS = (
    ("new", "New permit"),
    ("renewal", "Renewal permit"),
)

COMM_METHODS = (("email", "E-mail"), ("sms", "SMS"), ("postal", "Post"))

DATE_ESTIMATED_NA = (
    (NOT_APPLICABLE, "Not applicable"),
    ("not_estimated", "No."),
    ("D", "Yes, estimated the Day"),
    ("MD", "Yes, estimated Month and Day"),
    ("YMD", "Yes, estimated Year, Month and Day"),
)

DATE_ESTIMATED = (
    ("-", "No"),
    ("D", "Yes, estimated the Day"),
    ("MD", "Yes, estimated Month and Day"),
    ("YMD", "Yes, estimated Year, Month and Day"),
)

GENDER = (("male", "Male"), ("female", "Female"))

IDENTITY_TYPE = (
    ("OMANG", "Omang"),
    ("DRIVERS", "Driver's License"),
    ("PASSPORT", "Passport"),
    ("OMANG_RCPT", "Omang Receipt"),
    ("OTHER", "Other"),
)

MARITAL_STATUS = (
    ("single", "Single"),
    ("married", "Married"),
    ("widowed", "Widowed"),
    ("separated", "Separated"),
    ("divorced", "Divorced"),
)

PERMIT_TYPE = (("work", "Work"), ("residence", "Residence"))

POSTAL_PREFIX = (
    ("VB#", "VB#"),
    ("private_bag", "Private Bag"),
    ("p_o_box", "P. O. Box"),
)


PREFERRED_METHOD_COMM = (("sms", "SMS"), ("post", "POST"), ("email", "EMAIL"))

REASONS_PERMIT = (
    ("dependent", "Dependent"),
    ("volunteer", "Volunteer"),
    ("student", "Student"),
    ("immigrant", "Immigrant"),
    ("missionary", "Missionary"),
)

REPORT_STATUS = (
    (OPEN, "Open. Some information is still pending."),
    (CLOSED, "Closed. This report is complete"),
)

YES_NO = (("yes", "Yes"), ("no", "No"))

PERMIT_STATUS = (
    ("new", "New"),
    ("renewal", "Renewal"),
)
