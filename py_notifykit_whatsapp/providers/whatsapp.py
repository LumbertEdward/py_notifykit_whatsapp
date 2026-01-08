import requests
from py_notifykit_whatsapp.core import WhatsAppProvider
from py_notifykit_whatsapp.exceptions import WhatsAppProviderError


class MetaWhatsAppCloudProvider(WhatsAppProvider):
    BASE_URL = "https://graph.facebook.com/v22.0"

    def __init__(
        self,
        phone_number_id: str,
        access_token: str,
        timeout: int = 10,
    ):
        self.phone_number_id = phone_number_id
        self.access_token = access_token
        self.timeout = timeout

    @property
    def headers(self):
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

    def send_template(
        self,
        to: str,
        template_name: str,
        language: str = "en",
        parameters: list[str] = None,
    ) -> dict:
        try:
            payload = {
                "messaging_product": "whatsapp",
                "to": to,
                "type": "template",
                "template": {
                    "name": template_name,
                    "language": {"code": language},
                    "components": [
                        {
                            "type": "body",
                            "parameters": [
                                {"type": "text", "text": value}
                                for value in (parameters or [])
                            ],
                        }
                    ],
                },
            }

            response = requests.post(
                f"{self.BASE_URL}/{self.phone_number_id}/messages",
                json=payload,
                headers=self.headers,
                timeout=self.timeout,
            )

            response.raise_for_status()
            return response.json()

        except requests.RequestException as exc:
            raise WhatsAppProviderError(
                "Failed to send WhatsApp template message"
            ) from exc

    def send_attachment(self, to: str, attachment: dict) -> dict:
        try:
            payload = {
                "messaging_product": "whatsapp",
                "to": to,
                "type": "document",
                "document": {
                    "link": attachment["file_path"],
                    "caption": attachment.get("caption", ""),
                    "filename": attachment.get("name", "document"),
                },
            }

            response = requests.post(
                f"{self.BASE_URL}/{self.phone_number_id}/messages",
                json=payload,
                headers=self.headers,
                timeout=self.timeout,
            )

            response.raise_for_status()
            return response.json()

        except requests.RequestException as exc:
            raise WhatsAppProviderError("Failed to send WhatsApp attachment") from exc
