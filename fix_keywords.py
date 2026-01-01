import os
import re

# Define the keyword replacements
keyword_fixes = {
    'blog/free-qr-code-generator-with-logo-2025.html':
        'qr code with logo, branded qr code, custom qr code',
    'blog/how-qr-codes-help-business.html':
        'qr code for business, business card qr code, qr code marketing',
    'blog/qr-code-for-google-forms-2025.html':
        'qr code for google forms, survey qr code, feedback form qr code',
    'blog/qr-code-for-instagram-link-2025.html':
        'instagram qr code, qr code for instagram, grow instagram followers',
    'blog/qr-code-for-youtube-channel-2025.html':
        'youtube qr code, qr code for youtube, grow youtube subscribers',
    'blog/qr-code-wedding-invitations-2025.html':
        'wedding qr code, digital wedding invitation, wedding rsvp qr code',
    'blog/qr-codes-for-social-media-profiles.html':
        'qr code for social media, social media qr code',
    'blog/qr-codes-for-visiting-cards.html':
        'qr code for business cards, visiting card qr code',
    'blog/single-vs-multi-link-qr.html':
        'single link qr code, multi link qr code, qr code comparison',
    'blog/qr-code-menu-guide.html':
        'qr code for menu, restaurant qr code, contactless menu',
    'blog/qr-code-trends-2025.html':
        'qr code trends 2025, qr code technology',
    'blog/qr-codes-for-marketing-campaigns.html':
        'qr code marketing, marketing campaigns, promotional qr codes',
    'blog/qr-codes-for-payments.html':
        'qr code payment, payment qr code',
    'blog/qr-codes-for-portfolios.html':
        'qr code for portfolio, professional portfolio qr code',
    'blog/qr-codes-for-posters-and-flyers.html':
        'qr code for posters, marketing qr code',
    'blog/qr-codes-for-real-estate.html':
        'qr code for real estate, property qr code',
    'blog/qr-codes-for-restaurants.html':
        'qr code for restaurants, restaurant menu qr code',
    'blog/qr-codes-for-small-business-growth.html':
        'qr code for small business, small business growth',
    'blog/dynamic-vs-static-qr-codes.html':
        'dynamic qr code, static qr code, qr code types',
    'blog/how-to-create-a-professional-qr-code.html':
        'professional qr code, qr code design, qr code best practices',
}

def fix_keywords_in_file(filepath, new_keywords):
    """Fix keyword meta tag in a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Pattern to match keywords meta tag
        pattern = r'<meta name="keywords" content="[^"]*" />'
        replacement = f'<meta name="keywords" content="{new_keywords}" />'

        new_content = re.sub(pattern, replacement, content)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"[OK] Fixed: {filepath}")
        return True
    except Exception as e:
        print(f"[ERROR] Error fixing {filepath}: {e}")
        return False

def main():
    base_dir = os.path.dirname(__file__)
    fixed_count = 0

    print("Fixing keyword stuffing in blog posts...\n")

    for filename, new_keywords in keyword_fixes.items():
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            if fix_keywords_in_file(filepath, new_keywords):
                fixed_count += 1
        else:
            print(f"[SKIP] File not found: {filepath}")

    print(f"\n{'='*50}")
    print(f"Fixed {fixed_count}/{len(keyword_fixes)} files")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
