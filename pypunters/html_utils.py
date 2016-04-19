import re


def get_attributes(parent, selector, attribute):
	"""Get a list of attribute values for child elements of parent matching the given CSS selector"""

	return [child.get(attribute) for child in parent.cssselect(selector)]


def get_attribute(parent, selector, attribute, index=0):
	"""Get the attribute value for the child element of parent matching the given CSS selector

	If index is specified, return the attribute value for the matching child element with the specified zero-based index; otherwise, return the attribute value for the first matching child element.

	If selector is None, return the attribute value for parent instead.
	"""

	if selector is None:
		return parent.get(attribute)
	else:
		values = get_attributes(parent, selector, attribute)
		if (index < 0 and len(values) >= abs(index)) or (index >= 0 and len(values) > index):
			return values[index]


def parse_attributes(parent, selector, attribute, parser):
	"""Parse a list of attribute values for child elements of parent matching the given CSS selector"""

	values = []
	for value in get_attributes(parent, selector, attribute):
		try:
			values.append(parser(value))
		except ValueError:
			values.append(None)
	return values


def parse_attribute(parent, selector, attribute, parser, index=0):
	"""Parse the attribute value for the child element of parent matching the given CSS selector

	If index is specified, parse the attribute value for the matching child element with the specified zero-based index; otherwise, parse the attribute value for the first matching child element.

	If selector is None, parse the attribute value for parent instead.
	"""

	value = get_attribute(parent, selector, attribute, index)
	if value is not None:
		try:
			return parser(value)
		except ValueError:
			return None


def get_child(parent, selector, index=0):
	"""Get the child element of parent as specified by the given CSS selector

	If index is specified, return the matching child element at the specified zero-based index; otherwise, return the first matching child element.
	"""

	children = parent.cssselect(selector)
	if (index < 0 and len(children) >= abs(index)) or (index >= 0 and len(children) > index):
		return children[index]


def get_child_text(parent, selector, index=0):
	"""Get the text content of the child element of parent as specified by the given CSS selector

	If index is specified, return the text content of the matching child element at the specified zero-based index; otherwise, return the text content of the first matching child element.
	"""

	child = get_child(parent, selector, index)
	if child is not None:
		return child.text_content().strip()


def parse_child_text(parent, selector, parser, index=0):
	"""Parse the text content of the child element of parent as specified by the given CSS selector

	If index is specified, parse the text content of the matching child element at the specified zero-based index; otherwise, parse the text content of the first matching child element.
	"""

	text = get_child_text(parent, selector, index)
	if text is not None:
		try:
			return parser(text)
		except ValueError:
			return None


def get_child_match(parent, selector, pattern, index=0):
	"""Get a regex match for the text content of the child element of parent as specified by the given CSS selector

	If index is specified, return the regex match for the text content of the matching child element at the specified zero-based index; otherwise, return the regex match for the text content of the first matching child element.
	"""

	text = get_child_text(parent, selector, index)
	if text is not None:
		return re.search(pattern, text)


def get_child_match_groups(parent, selector, pattern, index=0):
	"""Get regex match groups for the text content of the child element of parent as specified by the given CSS selector

	If index is specified, return the regex match groups for the text content of the matching child element at the specified zero-based index; otherwise, return the regex match groups for the text content of the first matching child element.
	"""

	match = get_child_match(parent, selector, pattern, index)
	if match is not None:
		return match.groups()


def get_child_match_group(parent, selector, pattern, child_index=0, group_index=0):
	"""Get the regex match group with group_index for the text content of the child element of parent as specified by the given CSS selector

	If child_index is specified, return the regex match group with group_index for the text content of the child element at the specified zero-based index; otherwise, return the regex match group with group_index for the text content of the first matching child element.
	"""

	groups = get_child_match_groups(parent, selector, pattern, child_index)
	if groups is not None and ((group_index < 0 and len(groups) >= abs(group_index)) or (group_index >= 0 and len(groups) > group_index)):
		return groups[group_index]


def parse_child_match_group(parent, selector, pattern, parser, child_index=0, group_index=0):
	"""Parse the regex match group with group_index for the text content of the child element of parent as specified by the given CSS selector

	If child_index is specified, parse the regex match group with group_index for the text content of the child element at the specified zero-based index; otherwise, parse the regex match group with group_index for the text content of the first matching child element.
	"""

	value = get_child_match_group(parent, selector, pattern, child_index, group_index)
	if value is not None:
		try:
			return parser(value)
		except ValueError:
			return None