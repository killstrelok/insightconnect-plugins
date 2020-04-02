import komand
from .schema import DomainInput, DomainOutput, Input, Component

# Custom imports below
import whois
from komand.exceptions import PluginException


class Domain(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='domain',
            description=Component.DESCRIPTION,
            input=DomainInput(),
            output=DomainOutput())

    def run(self, params={}):
        domain = str(params.get(Input.DOMAIN))  # Comes in as unicode - whois library has assert for type on str
        self.logger.info(f"Getting whois information for {domain}")

        if not self.is_valid_domain(domain=domain):
            raise PluginException(cause="Invalid domain as input.",
                                  assistance="Ensure the domain is not prefixed with a protocol.")

        try:
            lookup_results = whois.query(domain, ignore_returncode=1)  # ignore_returncode required for plugin
        except Exception as e:
            self.logger.error(f"Error occurred: {e}")
            raise PluginException(cause="Error occurred", data=e)
        else:
            self.logger.info(f"lookup_results: {lookup_results}")
            serializable_results = lookup_results.get_json_serializable()
            serializable_results = komand.helper.clean_dict(serializable_results)

            return serializable_results

    @staticmethod
    def is_valid_domain(domain):
        if "://" in domain:
            return False
        return True
