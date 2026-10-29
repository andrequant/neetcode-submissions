class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        n = len(products)
        s = len(searchWord)

        out = []

        _prod = sorted(products)

        for i in range(s):

            sub = searchWord[:i+1]
            out.append([product for product in _prod if product.startswith(sub)][:3])
        
        return out

