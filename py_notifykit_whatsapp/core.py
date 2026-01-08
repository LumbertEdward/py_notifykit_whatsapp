from abc import ABC, abstractmethod
from typing import List, Dict, Optional


class WhatsAppProvider(ABC):
    """
    Abstract base class for WhatsApp providers.
    """

    @abstractmethod
    def send_template(
        self,
        to: str,
        template_name: str,
        language: str,
        parameters: List[str],
    ) -> Dict:
        """
        Send a WhatsApp template message.
        """
        pass

    @abstractmethod
    def send_attachment(
        self,
        to: str,
        attachment: Dict,
    ) -> Dict:
        """
        Send a WhatsApp attachment (document, image, video).
        """
        pass
