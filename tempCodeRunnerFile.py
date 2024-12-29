if sorted_recommendations:
            print(f"Recommended friends for {username} based on shared interests:")
        for user, shared_interests in sorted_recommendations.items():
            print(f"User: {user}, Shared Interests: {', '.join(shared_interests)}")
        else:
            print("No friend recommendations found based on shared interests.")
    
        return sorted_recommendations