# py_notifykit_whatsapp 💬

WhatsApp Cloud API integration for py_notifykit_whatsapp.

`py_notifykit_whatsapp` allows developers to send WhatsApp template messages and attachments
using Meta’s WhatsApp Cloud API through a clean, consistent Python interface.

---

## Features

- ✅ WhatsApp template messages
- ✅ Parameterized templates
- ✅ Document & media attachments
- ✅ Clean provider abstraction
- ✅ Easy to extend and test

---

## Installation

```bash
pip install py_notifykit_whatsapp
```

---

## Quick Start

Initialize the provider

---

```bash
from py_notifykit_whatsapp.providers.meta_cloud import MetaWhatsAppCloudProvider

whatsapp = MetaWhatsAppCloudProvider(
    phone_number_id="1234567890",
    access_token="YOUR_WHATSAPP_ACCESS_TOKEN",
)
```

---

## Send a template message

---

```bash
response = whatsapp.send_template(
    to="2547XXXXXXXX",
    template_name="payment_received",
    language="en",
    parameters=[
        "John Doe",
        "KES 1,500",
        "INV-2039",
    ],
)
```

---

## Send an attachment

```bash
response = whatsapp.send_attachment(
    to="2547XXXXXXXX",
    attachment={
        "file_path": "https://example.com/receipt.pdf",
        "name": "receipt.pdf",
        "caption": "Purchase Receipt",
    },
)
```

---

## Error Handling

All provider errors raise WhatsAppProviderError to ensure predictable behavior:

---

```bash
from py_notifykit_whatsapp.channels.whatsapp import WhatsAppProviderError

try:
    whatsapp.send_template(...)
except WhatsAppProviderError as exc:
    print(str(exc))
```
