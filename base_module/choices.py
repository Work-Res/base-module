
NOT_APPLICABLE = 'N/A'
OPEN = 'open'
CLOSED = 'closed'

DATE_ESTIMATED_NA = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('not_estimated', 'No.'),
    ('D', 'Yes, estimated the Day'),
    ('MD', 'Yes, estimated Month and Day'),
    ('YMD', 'Yes, estimated Year, Month and Day'),
)

DATE_ESTIMATED = (
    ('-', 'No'),
    ('D', 'Yes, estimated the Day'),
    ('MD', 'Yes, estimated Month and Day'),
    ('YMD', 'Yes, estimated Year, Month and Day'),
)

IDENTITY_TYPE = (
    ('OMANG', 'Omang'),
    ('DRIVERS', 'Driver\'s License'),
    ('PASSPORT', 'Passport'),
    ('OMANG_RCPT', 'Omang Receipt'),
    ('OTHER', 'Other'),
)


REPORT_STATUS = (
    (OPEN, 'Open. Some information is still pending.'),
    (CLOSED, 'Closed. This report is complete'),
)


APPLICATION_STATUS = (
	('new', 'New permit'),
	('renewal', 'Renewal permit'),
)

PREFERRED_METHOD_COMM = (
	('sms', 'SMS'),
	('post', 'POST'),
	('email', 'EMAIL')
)

YES_NO = (
	('yes', 'Yes'),
	('no', 'No')
)

REASONS_PERMIT = (
	('dependent', 'Dependent'),
	('volunteer', 'Volunteer'),
	('student', 'Student'),
	('immigrant', 'Immigrant'),
	('missionary', 'Missionary'),
)

GENDER = (
	('male', 'Male'),
	('female', 'Female')
)

PERMIT_TYPE = (
	('work', 'Work'),
	('residence', 'Residence')
)

MARITAL_STATUS = (
	('single', 'Single'),
	('married', 'Married'),
	('widowed', 'Widowed'),
	('separated', 'Separated'),
	('divorced', 'Divorced')
)
