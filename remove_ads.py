import os
import re

def comment_out_ads(filepath):
    """Comment out AdSense ad code in HTML files"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Pattern to match ad blocks with surrounding divs
        # This will match the entire ad container including the placeholder div
        pattern = r'(<div[^>]*>[\s\S]*?<!-- Ad Space[\s\S]*?<ins class="adsbygoogle"[\s\S]*?</script>[\s\S]*?</div>)'

        # Also match standalone ad blocks
        pattern2 = r'(<ins class="adsbygoogle"[\s\S]*?</script>)'

        # Comment out the matches
        new_content = re.sub(pattern, r'<!-- UNCOMMENT AFTER ADSENSE APPROVAL\n\1\n-->', content)
        new_content = re.sub(pattern2, r'<!-- UNCOMMENT AFTER ADSENSE APPROVAL: \1 -->', new_content)

        # Also comment out the AdSense script include
        script_pattern = r'(<script async src="https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js\?client=ca-pub-6077413695680101"[\s\S]*?</script>)'
        new_content = re.sub(script_pattern, r'<!-- UNCOMMENT AFTER ADSENSE APPROVAL:\n\1\n-->', new_content)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False
    except Exception as e:
        print(f"[ERROR] {filepath}: {e}")
        return False

def main():
    base_dir = os.path.dirname(__file__)

    # Get all HTML files
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html') and not file.startswith('fix_') and not file.startswith('remove_'):
                html_files.append(os.path.join(root, file))

    print(f"Found {len(html_files)} HTML files\n")
    print("Commenting out AdSense code (can be uncommented after approval)...\n")

    modified_count = 0
    for filepath in html_files:
        if comment_out_ads(filepath):
            rel_path = os.path.relpath(filepath, base_dir)
            print(f"[OK] {rel_path}")
            modified_count += 1

    print(f"\n{'='*60}")
    print(f"Modified {modified_count}/{len(html_files)} files")
    print(f"{'='*60}")
    print("\nNote: After AdSense approval, search for 'UNCOMMENT AFTER ADSENSE APPROVAL'")
    print("and uncomment those sections to enable ads.")

if __name__ == "__main__":
    main()
