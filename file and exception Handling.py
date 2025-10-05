# File Read & Write Challenge
def modify_file_content(content):
    """
    Modify the content of the file - you can customize this function
    This example converts text to uppercase and adds line numbers
    """
    lines = content.split('\n')
    modified_lines = []
    
    for i, line in enumerate(lines, 1):
        if line.strip():  # Only process non-empty lines
            modified_line = f"{i}: {line.upper()}"
            modified_lines.append(modified_line)
    
    return '\n'.join(modified_lines)

def file_read_write():
    """Read a file and write a modified version to a new file"""
    try:
        # Read from original file
        input_filename = input("Enter the input filename: ")
        
        with open(input_filename, 'r', encoding='utf-8') as file:
            original_content = file.read()
        
        print(f"Successfully read from {input_filename}")
        
        # Modify the content
        modified_content = modify_file_content(original_content)
        
        # Write to new file
        output_filename = input("Enter the output filename: ")
        
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        
        print(f"Successfully wrote modified content to {output_filename}")
        
        # Display preview
        print("\nPreview of modified content:")
        print("-" * 40)
        print(modified_content[:200] + "..." if len(modified_content) > 200 else modified_content)
        
    except FileNotFoundError:
        print("Error: The input file was not found.")
    except PermissionError:
        print("Error: Permission denied to read/write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
      
# Error Handling Lab 🧪
def safe_file_operations():
    """Handle file operations with comprehensive error handling"""
    
    while True:
        filename = input("\nEnter a filename to read (or 'quit' to exit): ")
        
        if filename.lower() == 'quit':
            print("Goodbye!")
            break
        
        try:
            # Try to open and read the file
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # If successful, display file info
            print(f"\n✅ Successfully opened '{filename}'")
            print(f"📊 File size: {len(content)} characters")
            print(f"📝 Number of lines: {len(content.splitlines())}")
            
            # Display first few lines as preview
            lines = content.splitlines()
            print("\n📖 First 5 lines of the file:")
            print("-" * 40)
            for i, line in enumerate(lines[:5], 1):
                print(f"{i}: {line}")
            if len(lines) > 5:
                print("... (file continues)")
                
            # Ask if user wants to see more options
            show_more_options(filename, content)
            
        except FileNotFoundError:
            print(f"❌ Error: The file '{filename}' was not found.")
            print("💡 Please check the filename and try again.")
            
        except PermissionError:
            print(f"❌ Error: Permission denied to read '{filename}'.")
            print("💡 Check if the file is open in another program or if you have read permissions.")
            
        except UnicodeDecodeError:
            print(f"❌ Error: Cannot decode '{filename}'. It might be a binary file.")
            print("💡 Try specifying a different encoding or choose a text file.")
            
        except IsADirectoryError:
            print(f"❌ Error: '{filename}' is a directory, not a file.")
            
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
            print("💡 Please try again with a different file.")

def show_more_options(filename, content):
    """Show additional file operations"""
    while True:
        print("\nAdditional options:")
        print("1. Count words in file")
        print("2. Search for text in file")
        print("3. Save statistics to new file")
        print("4. Choose another file")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            word_count = len(content.split())
            print(f"📊 Total words in file: {word_count}")
            
        elif choice == '2':
            search_term = input("Enter text to search for: ")
            if search_term in content:
                occurrences = content.count(search_term)
                print(f"🔍 Found '{search_term}' {occurrences} time(s) in the file")
            else:
                print(f"🔍 '{search_term}' not found in the file")
                
        elif choice == '3':
            try:
                stats_filename = f"{filename}_stats.txt"
                with open(stats_filename, 'w') as stats_file:
                    stats_file.write(f"File Statistics for: {filename}\n")
                    stats_file.write(f"Total characters: {len(content)}\n")
                    stats_file.write(f"Total lines: {len(content.splitlines())}\n")
                    stats_file.write(f"Total words: {len(content.split())}\n")
                print(f"✅ Statistics saved to {stats_filename}")
            except Exception as e:
                print(f"❌ Error saving statistics: {e}")
                
        elif choice == '4':
            break
        else:
            print("❌ Invalid choice. Please enter 1-4.")

# Run the error handling lab
if __name__ == "__main__":
    file_read_write()
    print("🔍 File Reader with Error Handling")
    print("=" * 40)
    safe_file_operations()
    
