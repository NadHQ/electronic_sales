from io import BytesIO

import qrcode


class QrCodeBuilder:
    def __init__(self, data) -> None:
        self.data = data

    def _build(self, data: str) -> BytesIO:
        # Создаем QR-код
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        return buffer

    def build_contacts_qr_code(self, data: dict) -> BytesIO:
        contact_info = f"""
        Email: {data.get('email', '')}
        Country: {data.get('country', '')}
        City: {data.get('city', '')}
        Street: {data.get('street', '')}
        Building number: {data.get('building_number', '')}
        """
        return self._build(contact_info)
