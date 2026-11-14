
from abc import ABC, abstractmethod


# Classe abstraite Paiement
class Paiement(ABC):

    def __init__(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit etre positif")

        self._montant = montant

    @abstractmethod
    def payer(self):
        pass


# Classe CarteBancaire
class CarteBancaire(Paiement):

    def __init__(self, montant, numero, cvv):
        super().__init__(montant)
        self.numero = numero
        self.cvv = cvv

    def payer(self):
        return f"Paiement par carte bancaire de {self._montant} DH confirme."


# Classe PayPal
class PayPal(Paiement):

    def __init__(self, montant, email, token):
        super().__init__(montant)
        self.email = email
        self.token = token

    def payer(self):
        return f"Paiement PayPal de {self._montant} DH confirme."


# Classe Crypto
class Crypto(Paiement):

    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)
        self.wallet_id = wallet_id
        self.reseau = reseau

    def payer(self):
        return f"Paiement Crypto ({self.reseau}) de {self._montant} DH confirme."


# Fonction de traitement des paiements
def traiter_paiements(liste):

    for paiement in liste:
        print(paiement.payer())


# Programme principal
if __name__ == "__main__":

    paiements = [
        CarteBancaire(250, "123456789", "123"),
        CarteBancaire(500, "987654321", "456"),

        PayPal(150, "mohamed@gmail.com", "123"),
        PayPal(300, "ennassiry@gmail.com", "456"),

        Crypto(200, "wallet001", "BTC"),
        Crypto(400, "wallet002", "ETH")
    ]

    traiter_paiements(paiements)
