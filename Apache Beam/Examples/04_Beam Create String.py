import apache_beam as beam

def main():
    """
    Apache Beam Example: Creating and Processing String PCollections
    
    This example demonstrates:
    1. Creating PCollections from string lists
    2. String transformations (uppercase, lowercase)
    3. String filtering based on length
    4. String formatting and manipulation
    """
    
    print("=== Apache Beam: Create and Process Strings ===")
    
    with beam.Pipeline() as p:
        # Create a PCollection of fruit names
        fruits = p | 'Create fruit strings' >> beam.Create([
            'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape'
        ])
        
        # Example 1: Print original strings
        print("\n1. Original fruit names:")
        fruits | 'Print original fruits' >> beam.Map(lambda x: print(f"   {x}"))
        
        # Example 2: Convert to uppercase
        print("\n2. Uppercase fruit names:")
        uppercase_fruits = (
            fruits 
            | 'Convert to uppercase' >> beam.Map(str.upper)
            | 'Print uppercase fruits' >> beam.Map(lambda x: print(f"   {x}"))
        )
        
        # Example 3: Filter strings by length (fruits with 5+ characters)
        print("\n3. Fruits with 5+ characters:")
        long_fruits = (
            fruits 
            | 'Filter long fruit names' >> beam.Filter(lambda x: len(x) >= 5)
            | 'Print long fruits' >> beam.Map(lambda x: print(f"   {x} ({len(x)} chars)"))
        )
        
        # Example 4: Format strings with additional information
        print("\n4. Formatted fruit information:")
        formatted_fruits = (
            fruits 
            | 'Format fruit info' >> beam.Map(lambda x: f"Fruit: {x.title()}, Length: {len(x)}, First Letter: {x[0].upper()}")
            | 'Print formatted fruits' >> beam.Map(lambda x: print(f"   {x}"))
        )
        
        # Example 5: Create sentences from fruit names
        print("\n5. Fruit sentences:")
        fruit_sentences = (
            fruits 
            | 'Create sentences' >> beam.Map(lambda x: f"I love eating {x}s!")
            | 'Print sentences' >> beam.Map(lambda x: print(f"   {x}"))
        )

if __name__ == "__main__":
    main()
