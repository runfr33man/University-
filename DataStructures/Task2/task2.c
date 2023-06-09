#include<stdio.h> 
#include<stdlib.h>
#include<stdbool.h> 

struct node 
{ 
    char key[255];
    char gkey[255]; 
    struct node *left, *right; 
}; 
   

struct node *newNode(char *item[], char*gitem[]) 
{ 
    struct node *temp =  (struct node *)malloc(sizeof(struct node)); 
    strcpy(temp->key,item);
    strcpy(temp->gkey,gitem); 
    temp->left = temp->right = NULL; 
    return temp; 
} 
   

int inorder(struct node *root) 
{ 
    int c = 0; 
    if (root != NULL) 
    { 
        inorder(root->left); 
        printf("%s \n", root->key); 
        c++;
        inorder(root->right); 
    } 
    return c;
} 
   

struct node* insert(struct node* node, char *key[], char *gkey[]) 
{ 

    if (node == NULL)
    {
        return newNode(key, gkey); 
    }
    int ret = strcmp(key, node->key);
    if (ret < 0) 
    {
        node->left  = insert(node->left, key, gkey); 
    }
    else if (ret > 0)
    {
        node->right = insert(node->right, key, gkey);    
    }
    else
    {
        printf("String already exists \n");
    }
    
    return node; 
} 

struct node * minValueNode(struct node* node) 
{ 
    struct node* current = node; 
  
    /* loop down to find the leftmost leaf */
    while (current && current->left != NULL) 
        current = current->left; 
  
    return current; 
} 
  
struct node* deleteNode(struct node* root, char *key[]) 
{ 
    if (root == NULL)
    {
        return root; 
    }
    
    int ret = strcmp(key, root->key);
    if (ret < 0) 
    {
        root->left = deleteNode(root->left, key); 
    }
    else if (ret > 0 ) 
    {
        root->right = deleteNode(root->right, key); 
    }
    else
    { 
        // node with only one child or no child 
        if (root->left == NULL) 
        { 
            struct node *temp = root->right; 
            free(root); 
            return temp; 
        } 
        else if (root->right == NULL) 
        { 
            struct node *temp = root->left; 
            free(root); 
            return temp; 
        } 
  
        // node with two children: Get the inorder successor (smallest 
        // in the right subtree) 
        struct node* temp = minValueNode(root->right); 
  
        // Copy the inorder successor's content to this node 
        strcpy(root->key, temp->key); 

        // Delete the inorder successor 
        root->right = deleteNode(root->right, temp->key); 
    } 
    return root; 
} 


//---------------
struct node* print2DUtil(struct node* root, int space, int COUNT) 
{ 
    // Base case 
    //COUNT = inorder(root);
    // Increase distance between levels 
    if (root == NULL) 
        return 0; 
    space += COUNT; 
  
    // Process right child first 
    print2DUtil(root->right, space, COUNT); 
  
    // Print current node after space 
    // count 
    printf("\n"); 
    for (int i = COUNT; i < space; i++)
    {
        printf("          "); 
    }
    printf("%s \n", root->key); 
  
    // Process left child 
    print2DUtil(root->left, space, COUNT); 
} 
//---------------




int inorderC(struct node *root, char *word[]) 
{ 
    char x[255];
    int j =0;
    if (root != NULL) 
    { 
        
        inorderC(root->left, word);

        strcpy(x , root->key);
        if(strstr(x, word) != NULL)
        {
            printf("English word: |    %s      |Tranlsation: |    %s \n", root->key, root->gkey); 
        }
        inorderC(root->right, word); 
    } 
    return 0;
} 





int main() 
{ 
    struct node *root = NULL; 
    root = insert(root, "gravity", "βαρύτητα");
    insert(root, "gin", "τζιν"); 
    insert(root, "gintonic", "τζιντόνικ");
    insert(root, "gravel", "χαλίκι");
    insert(root, "cityseventeen", "πόλη17");
    insert(root, "mother", "μητέρα"); 
    insert(root, "black", "μαύρος"); 
    insert(root, "mirror", "καθρεύτης");
    insert(root, "cyberpunk2077", "σάιμπερπανκ2077");
    insert(root, "cyberpunk", "σάιμπερπανκ");
    insert(root, "twotowers", "δύοπύργοι");
    insert(root, "thecakeisaliethecakeisaliethecakeisalie", "τοκέικείναιψέματοκέικείναιψέματοκέικείναιψέμα");
    char word[255];
    char gword[255];
    int COUNT = inorder(root);
    while(true)
    {
        //COUNT = inorder(root);
        printf("Choose one from the following actions: \n 1:Insert element \n 2:Delete element \n 3:Search element \n 4:Print Binary tree \n 0:Exit system: ");
        int ans = 0;
        scanf("%d", &ans);
        switch (ans)
        {
            case 1:
                printf("Please insert(creates new node) the english word (Use only characters): ");
                scanf("%s", word);
                printf("Please insert(creates new node) the greek word (Use only characters): ");
                scanf("%s", gword);
                insert(root, word, gword);
                break;

            case 2:
                printf("Please delete(deletes a node) a word (Use only characters): ");
                scanf("%s", word);
                deleteNode(root, word);
                break;

            case 3:
                printf("Please input chars (search based on chars): ");
                scanf("%s", word);
                ans = strlen(word);
                inorderC(root, word);
                break;

            case 4:
                print2DUtil(root,0, COUNT);
                break;

            default:
                exit(EXIT_SUCCESS);
                break;
        }
    } 
   
    return 0; 
} 
