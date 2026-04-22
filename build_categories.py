import sys, re, random

configs = {
    'baskets.html': ('BA', 12, 'basket'),
    'crochet.html': ('CR', 12, 'crochet'),
    'jewelry.html': ('JW', 12, 'jewelry'),
    'pottery.html': ('PB', 12, 'pottery'),
    'resin.html': ('RA', 12, 'resin'),
    'walldecor.html': ('wallHA', 9, 'walldecor')
}

name_parts = {
    'basket': {
        'adj': ['Woven', 'Boho', 'Rustic', 'Handwoven', 'Natural', 'Minimalist', 'Cozy', 'Earthy', 'Coastal'],
        'noun': ['Seagrass Basket', 'Jute Storage', 'Macrame Bin', 'Cotton Rope Basket', 'Rattan Hamper', 'Bamboo Basket']
    },
    'crochet': {
        'adj': ['Cozy', 'Pastel', 'Vintage', 'Chunky', 'Soft', 'Bohemian', 'Floral', 'Warm'],
        'noun': ['Tote Bag', 'Daisy Bouquet', 'Winter Scarf', 'Throw Blanket', 'Amigurumi Plush', 'Bucket Hat']
    },
    'jewelry': {
        'adj': ['Elegant', 'Boho', 'Minimalist', 'Dainty', 'Vintage', 'Sparkling', 'Artisan', 'Rustic'],
        'noun': ['Pendant Necklace', 'Drop Earrings', 'Beaded Choker', 'Silver Ring', 'Charm Bracelet', 'Hoop Earrings']
    },
    'pottery': {
        'adj': ['Speckled', 'Earthy', 'Glazed', 'Matte', 'Rustic', 'Terracotta', 'Ceramic', 'Hand-thrown'],
        'noun': ['Clay Mug', 'Matcha Bowl', 'Minimalist Vase', 'Dinner Plate', 'Planter Pot', 'Incense Holder']
    },
    'resin': {
        'adj': ['Ocean', 'Floral', 'Gold Leaf', 'Luminous', 'Glitter', 'Pastel', 'Crystal', 'Marble'],
        'noun': ['Coaster Set', 'Serving Tray', 'Wall Clock', 'Jewelry Dish', 'Bookmark', 'Geode Art']
    },
    'walldecor': {
        'adj': ['Boho', 'Rustic', 'Macrame', 'Woven', 'Minimal', 'Earthy', 'Botanical'],
        'noun': ['Dreamcatcher', 'Wall Hanging', 'Tapestry', 'Floating Shelf', 'Sun & Moon Mirror', 'Art Print']
    }
}

def generate_name(cat, seed_val):
    random.seed(seed_val)
    adj = random.choice(name_parts[cat]['adj'])
    noun = random.choice(name_parts[cat]['noun'])
    return f"{adj} {noun}"

def process_file(filepath):
    prefix, count, cat = configs[filepath]
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_grid = '<div class="product-grid-new">\n'
    for i in range(1, count + 1):
        filename = f"{prefix}{i}.jpeg"
        base_id = f"{prefix}{i}"
        
        delay = 50 + ((i - 1) % 4) * 50
        
        prod_name = generate_name(cat, base_id)
        
        random.seed(base_id)
        price = random.choice([299, 349, 399, 499, 599, 799, 899, 1299, 1499, 1999, 2499])
        wa_text = f"Hi! I would like to purchase the item '{prod_name}' ({base_id}) priced at ₹{price}."
        wa_link = f"https://wa.me/919876543210?text={wa_text.replace(' ', '%20')}"
        
        new_grid += f'''        <div class="product-item-new" data-aos="fade-up" data-aos-delay="{delay}">
          <div class="img-wrap">
            <img src="Images/{filename}" alt="{prod_name}" onerror="this.onerror=null; this.src='Images/1.jpeg';">
          </div>
          <div class="prod-details" style="padding: 16px; text-align: center; border-top: 1px solid rgba(0,0,0,0.05);">
            <div class="prod-name" style="font-weight: 600; color: var(--primary-purple); font-size: 1.1rem; margin-bottom: 4px;">{prod_name}</div>
            <div class="prod-price" style="font-weight: 800; color: var(--rose); font-size: 1.15rem; margin-bottom: 14px;">₹{price}</div>
            <a href="{wa_link}" target="_blank" class="btn btn-wa" style="display: flex; justify-content: center; align-items: center; gap: 8px; font-size: 0.9rem; padding: 10px; width: 100%; border-radius: 8px;">
              <i class="fab fa-whatsapp" style="font-size: 1.1rem;"></i> Buy Now
            </a>
          </div>
        </div>\n'''
        
    new_grid += '      </div>\n      '
    
    # We want to replace whatever grid sits between the text-center div and the Custom Order CTA
    pattern = re.compile(r'(<div class="text-center"[^>]*>.*?</div>).*?(<!-- Custom Order CTA -->)', re.DOTALL)
    
    match = pattern.search(content)
    if match:
        # Construct the new section body
        new_content = content[:match.end(1)] + "\n      " + new_grid + "\n      " + content[match.start(2):]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Processed {filepath}")
    else:
        print(f"Failed to match in {filepath}")

if __name__ == '__main__':
    for f in configs.keys():
        process_file(f)
