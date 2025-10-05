import requests
import os
from urllib.parse import urlparse
from pathlib import Path

def download_image_from_url():
    """
    Downloads an image from a URL and saves it to Fetched_Images directory
    """
    print("🖼️  Image Downloader")
    print("=" * 40)
    
    # Get URL from user
    url = input("Please enter the image URL: ").strip()
    
    if not url:
        print("❌ Error: No URL provided!")
        return
    
    try:
        # Create directory if it doesn't exist
        image_dir = "Fetched_Images"
        os.makedirs(image_dir, exist_ok=True)
        print(f"📁 Directory '{image_dir}' is ready!")
        
        # Send GET request with headers to mimic a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        print("🌐 Connecting to the server...")
        response = requests.get(url, headers=headers, timeout=30, stream=True)
        
        # Check if request was successful
        response.raise_for_status()
        
        # Check if content is actually an image
        content_type = response.headers.get('content-type', '')
        if not content_type.startswith('image/'):
            print("❌ Error: The URL does not point to an image file!")
            print(f"   Content-Type received: {content_type}")
            return
        
        # Extract filename from URL or generate one
        filename = extract_filename(url, content_type)
        filepath = os.path.join(image_dir, filename)
        
        # Check if file already exists
        if os.path.exists(filepath):
            overwrite = input(f"⚠️  File '{filename}' already exists. Overwrite? (y/n): ").lower()
            if overwrite != 'y':
                print("📝 Operation cancelled by user.")
                return
        
        # Download and save the image
        print(f"💾 Downloading image as '{filename}'...")
        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        
        # Verify the file was saved
        file_size = os.path.getsize(filepath)
        print(f"✅ Success! Image saved to: {filepath}")
        print(f"📊 File size: {file_size:,} bytes")
        
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
        print("💡 Please check the URL and try again.")
        
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Unable to reach the server.")
        print("💡 Check your internet connection and the URL.")
        
    except requests.exceptions.Timeout:
        print("❌ Timeout Error: The request took too long.")
        print("💡 The server might be busy. Try again later.")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Request Error: {e}")
        
    except PermissionError:
        print("❌ Permission Error: Cannot write to the directory.")
        print("💡 Check your file permissions.")
        
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

def extract_filename(url, content_type):
    """
    Extracts filename from URL or generates one based on content type
    """
    # Parse the URL
    parsed_url = urlparse(url)
    
    # Try to get filename from URL path
    path = parsed_url.path
    if path and '/' in path:
        filename = path.split('/')[-1]
        if filename and '.' in filename:
            return filename
    
    # Generate filename based on content type
    extension = get_extension_from_content_type(content_type)
    import time
    timestamp = int(time.time())
    return f"image_{timestamp}{extension}"

def get_extension_from_content_type(content_type):
    """
    Maps content type to file extension
    """
    extension_map = {
        'image/jpeg': '.jpg',
        'image/jpg': '.jpg',
        'image/png': '.png',
        'image/gif': '.gif',
        'image/webp': '.webp',
        'image/svg+xml': '.svg',
        'image/bmp': '.bmp',
        'image/tiff': '.tiff'
    }
    
    return extension_map.get(content_type.lower(), '.jpg')  # Default to .jpg

def batch_download_mode():
    """
    Optional: Allows downloading multiple images
    """
    print("\n🎯 BATCH DOWNLOAD MODE")
    print("Enter multiple URLs (one per line). Type 'done' when finished.")
    
    urls = []
    while True:
        url = input("Enter URL (or 'done' to finish): ").strip()
        if url.lower() == 'done':
            break
        if url:
            urls.append(url)
    
    print(f"\n📥 Preparing to download {len(urls)} images...")
    
    success_count = 0
    for i, url in enumerate(urls, 1):
        print(f"\n--- Downloading image {i}/{len(urls)} ---")
        # This would call a modified version of download_image_from_url
        # that accepts URL as parameter instead of user input
        print(f"URL: {url}")
        # download_single_image(url)  # You could implement this function
    
    print(f"\n🎉 Download complete! {success_count}/{len(urls)} images downloaded successfully.")

def main():
    """
    Main function with menu
    """
    while True:
        print("\n" + "=" * 50)
        print("🖼️  IMAGE DOWNLOADER MENU")
        print("=" * 50)
        print("1. Download single image")
        print("2. Batch download multiple images")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            download_image_from_url()
        elif choice == '2':
            batch_download_mode()
        elif choice == '3':
            print("👋 Thank you for using Image Downloader!")
            break
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

# Alternative function for programmatic use
def download_single_image(url, download_dir="Fetched_Images"):
    """
    Function to download a single image without user interaction
    Useful for embedding in other scripts
    """
    try:
        os.makedirs(download_dir, exist_ok=True)
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        content_type = response.headers.get('content-type', '')
        if not content_type.startswith('image/'):
            raise ValueError(f"URL does not point to an image. Content-Type: {content_type}")
        
        filename = extract_filename(url, content_type)
        filepath = os.path.join(download_dir, filename)
        
        # Handle filename conflicts
        counter = 1
        name, ext = os.path.splitext(filename)
        while os.path.exists(filepath):
            filename = f"{name}_{counter}{ext}"
            filepath = os.path.join(download_dir, filename)
            counter += 1
        
        with open(filepath, 'wb') as file:
            file.write(response.content)
        
        return filepath
        
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None

if __name__ == "__main__":
    # Install requests if not available
    try:
        import requests
    except ImportError:
        print("❌ The 'requests' library is required but not installed.")
        print("💡 Install it using: pip install requests")
        exit(1)
    
    main()
