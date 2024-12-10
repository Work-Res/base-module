from django.utils.http import url_has_allowed_host_and_scheme
from urllib.parse import urlencode, urlparse, parse_qs
from django.http import HttpResponseRedirect


class BaseUrlModelAdminMixin:
    """
    Mixin to handle safe redirection with additional query parameters
    for Django admin actions.
    """

    def get_safe_next_url(self, request, fallback_url='/workresdashboard/'):
        """
        Extract and validate the 'next' parameter from the request to ensure it's safe.

        Args:
            request (HttpRequest): The HTTP request object.
            fallback_url (str): The fallback URL if 'next' is invalid or not provided.

        Returns:
            str: A safe URL for redirection.
        """
        next_url = request.GET.get('next', fallback_url)
        if url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
            return next_url
        return fallback_url

    def append_query_parameters(self, next_url, extra_params):
        """
        Append additional query parameters to the next URL.

        Args:
            next_url (str): The base URL for redirection.
            extra_params (dict): Additional query parameters to append.

        Returns:
            str: The updated URL with query parameters.
        """
        parsed_url = urlparse(next_url)
        existing_params = parse_qs(parsed_url.query)
        updated_params = {**existing_params, **extra_params}
        new_query_string = urlencode(updated_params, doseq=True)
        return parsed_url._replace(query=new_query_string).geturl()

    def response_add(self, request, obj, post_url_continue=None):
        """
        Handle redirect after adding an object, passing along query parameters.
        """
        next_url = self.get_safe_next_url(request)
        extra_params = {'new_id': obj.id}  # Example: Pass the new object ID
        return HttpResponseRedirect(self.append_query_parameters(next_url, extra_params))

    def response_change(self, request, obj):
        """
        Handle redirect after editing an object, passing along query parameters.
        """
        next_url = self.get_safe_next_url(request)
        extra_params = {'changed_id': obj.id}  # Example: Pass the updated object ID
        return HttpResponseRedirect(self.append_query_parameters(next_url, extra_params))

    def response_delete(self, request, obj_display, obj_id):
        """
        Handle redirect after deleting an object, passing along query parameters.
        """
        next_url = self.get_safe_next_url(request)
        extra_params = {'deleted_id': obj_id}  # Example: Pass the deleted object ID
        return HttpResponseRedirect(self.append_query_parameters(next_url, extra_params))
